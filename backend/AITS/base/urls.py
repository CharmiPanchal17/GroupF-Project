from django.urls import path
from .views import (
    RegisterStudentView,
    RegisterLecturerView,
    RegisterRegistrarView,
    LoginView,
    VerifyEmailView,
    ResendVerificationEmailView
)
from rest_framework_simplejwt.views import TokenRefreshView

app_name = 'base'

urlpatterns = [
    path('register/student/', RegisterStudentView.as_view(), name='register-student'),
    path('register/lecturer/', RegisterLecturerView.as_view(), name='register-lecturer'),
    path('register/registrar/', RegisterRegistrarView.as_view(), name='register-registrar'),

    path('login/', LoginView.as_view(), name='login'),

    path('login/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    path('verify-email/', VerifyEmailView.as_view(), name='verify-email'),
    path('resend-verification/', ResendVerificationEmailView.as_view(), name='resend-verification'),
]