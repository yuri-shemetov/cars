from django.urls import path

from .views import LoginAPIView, RegistrationAPIView, UserRetrieveUpdateAPIView

app_name = 'auth'
urlpatterns = [
    path('user/', UserRetrieveUpdateAPIView.as_view(), name='about_user'),
    path('user/registration/', RegistrationAPIView.as_view()),
    path('user/login/', LoginAPIView.as_view()),
]
