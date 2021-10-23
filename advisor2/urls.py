from django.contrib import admin
from django.urls import path
from .views import AdvisorView

urlpatterns = [
    path('advisor', AdvisorView.as_view())
]
