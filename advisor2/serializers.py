from django.db import models
from django.db.models import fields
from rest_framework import serializers

from users.serializers import UserSerializer
from .models import Advisor, Booking


class AdvisorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advisor
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    # advisor = AdvisorSerializer(read_only=True)
    class Meta:
        model = Booking
        fields = '__all__'

    # Explaination - https://stackoverflow.com/questions/50256852/django-rest-framework-post-foreign-key
    def to_representation(self, instance):
        self.fields['advisor'] =  AdvisorSerializer(read_only=True)
        # self.fields['user'] = UserSerializer(read_only=True)
        return super(BookingSerializer, self).to_representation(instance)
