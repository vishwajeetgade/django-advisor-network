from django.urls import path
from .views import GetAdvisorView, LoginView, RegisterView, bookAdvisorMeetingDate, getBookingOfUser

urlpatterns = [
    path('<str:user_id>/advisor/booking', getBookingOfUser.as_view()),
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
    path('<str:user_id>/advisor', GetAdvisorView.as_view()),
    path('<str:user_id>/advisor/<str:advisor_id>', bookAdvisorMeetingDate.as_view())
]
