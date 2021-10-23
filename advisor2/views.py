from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from advisor2.serializers import AdvisorSerializer

# Create your views here.
class AdvisorView(APIView):
    def post(self, request):
        serializer = AdvisorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"success": True}, status=status.HTTP_200_OK)
