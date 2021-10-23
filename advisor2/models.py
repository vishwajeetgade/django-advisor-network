from django.db import models
from users.models import User

# Create your models here.

class Advisor(models.Model):
    name=models.CharField(max_length=255)
    photo=models.URLField()

class Booking(models.Model):
    user=models.ForeignKey(User, related_name='users', blank=True, null=True, on_delete=models.CASCADE)
    advisor=models.ForeignKey(Advisor, related_name='advisors', blank=True, null=True, on_delete=models.CASCADE)
    booking_time=models.DateTimeField()