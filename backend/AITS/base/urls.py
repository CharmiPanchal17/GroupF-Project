from django.urls import path
from .views import (
    RegisterStudentView,
    RegisterLecturerView,
    RegisterRegistrarView,
    LoginView,
    VerifyEmailView,
    ResendVerificationEmailView,
    LogoutView,  
    PasswordResetRequestView,  
    PasswordResetConfirmView  
)
from rest_framework_simplejwt.views import TokenRefreshView

app_name = 'base'

urlpatterns = [
    # Registration
    path('register/student/', RegisterStudentView.as_view(), name='register-student'),
    path('register/lecturer/', RegisterLecturerView.as_view(), name='register-lecturer'),
    path('register/registrar/', RegisterRegistrarView.as_view(), name='register-registrar'),

    # Authentication
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),  
    path('login/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Email Verification
    path('verify-email/', VerifyEmailView.as_view(), name='verify-email'),
    path('resend-verification/', ResendVerificationEmailView.as_view(), name='resend-verification'),

    # Password Reset
    path('password-reset/', PasswordResetRequestView.as_view(), name='password-reset'),
    path('password-reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password-reset-confirm'),
]
