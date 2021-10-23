from django.http import response
from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from advisor2.serializers import AdvisorSerializer, BookingSerializer
from users.models import User
from advisor2.models import Advisor, Booking
from users.serializers import UserSerializer
import jwt
import datetime

# Create your views here.


class RegisterView(APIView):
    def post(self, request):
        # serializer is use to convert models data in JSON Object
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        print(serializer.data['id'])
        payload = {
            'id': serializer.data['id'],
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret',
                           algorithm='HS256').decode('utf-8')
        response = Response()

        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'jwt': token
        }

        return response


class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        if email == "" or password == "":
            return Response({"success": False, "message": "Some field are missing"}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.filter(email=email).first()

        if user is None:
            return Response({"success": False, "message": "User not found"}, status=status.HTTP_401_UNAUTHORIZED)

        if not user.check_password(password):
            return Response({"success": False, "message": "Invalid Credentials"}, status=status.HTTP_401_UNAUTHORIZED)

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret',
                           algorithm='HS256').decode('utf-8')
        response = Response()
        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'jwt': token
        }

        return response


class GetAdvisorView(APIView):
    def get(self, request, user_id):
        token = request.COOKIES.get('jwt')

        if not token:
            return Response({"success": False, "message": "UnAuthorized"}, status=status.HTTP_401_UNAUTHORIZED)

        try:
            payload = jwt.decode(token, 'secret', alogrithm=['HS256'])
        except jwt.ExpiredSignatureError:
            return Response({"success": False, "message": "UnAuthorized"}, status=status.HTTP_401_UNAUTHORIZED)

        advisor = Advisor.objects.all()
        # serializer is use to convert models data in JSON Object
        # many=True is use to query array of data
        serializer = AdvisorSerializer(advisor, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class bookAdvisorMeetingDate(APIView):
    def post(self, request, user_id, advisor_id):
        token = request.COOKIES.get('jwt')

        if not token:
            return Response({"success": False, "message": "UnAuthorized"}, status=status.HTTP_401_UNAUTHORIZED)

        try:
            payload = jwt.decode(token, 'secret', alogrithm=['HS256'])
        except jwt.ExpiredSignatureError:
            return Response({"success": False, "message": "UnAuthorized"}, status=status.HTTP_401_UNAUTHORIZED)

        if not str(payload['id']) == user_id:
            return Response({"success": False, "message": "UnAuthorized | You have no access to this route"}, status=status.HTTP_401_UNAUTHORIZED)
        # print(user_id, advisor_id)
        user = User.objects.filter(id=user_id).first()
        advisor = Advisor.objects.filter(id=advisor_id).first()
        print('user adn advisor', user.id, advisor.id)
        data = {**request.data, 'user': user_id, 'advisor': advisor_id}
        serializer = BookingSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        

        return Response({"success": True}, status=status.HTTP_200_OK)


class getBookingOfUser(APIView):
    def get(self, request, user_id):
        token = request.COOKIES.get('jwt')

        if not token:
            return Response({"success": False, "message": "UnAuthorized"}, status=status.HTTP_401_UNAUTHORIZED)
        try:
            payload = jwt.decode(token, 'secret', alogrithm=['HS256'])
        except jwt.ExpiredSignatureError:
            return Response({"success": False, "message": "UnAuthorized"}, status=status.HTTP_401_UNAUTHORIZED)
        # print(type(str(payload['id'])), type(user_id))
        if not str(payload['id']) == user_id:
            return Response({"success": False, "message": "UnAuthorized | You have no access to this route"}, status=status.HTTP_401_UNAUTHORIZED)


        booking = Booking.objects.filter(user_id=user_id)
        # if booking is None:
        #     return Response({[]}, status=status.HTTP_200_OK)
        

        serializer = BookingSerializer(booking, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
