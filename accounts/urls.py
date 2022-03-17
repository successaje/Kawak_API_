from django.urls import path, include

from .views import RegisterView, VerifyEmail, LoginAPIView, PasswordTokenCheckAPI, RequestPasswordResetEmail, SetNewPasswordAPIView

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('register/', RegisterView.as_view(), name ='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('email-verify/', VerifyEmail.as_view(), name ='email-verify'),
    path('token/refresh/', TokenRefreshView.as_view(), name = 'token'),
    path('request-reset-email/', RequestPasswordResetEmail.as_view(), name = 'request_reset_email'),
    path('password-reset/<uidb64>/<token>/', PasswordTokenCheckAPI.as_view(), name = 'password-reset-confirm'),
    path('password-reset-complete/', SetNewPasswordAPIView.as_view(), name = '')
]