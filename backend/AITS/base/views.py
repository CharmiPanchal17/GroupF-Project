from rest_framework import permissions, generics, status, views
from rest_framework.views import APIView
from django.contrib.auth import authenticate, get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import get_object_or_404
import jwt
from django.conf import settings
from .serializers import (
    StudentRegistrationSerializer,
    LecturerRegistrationSerializer,
    RegistrarRegistrationSerializer,
    VerificationSerializer,
    ResendVerificationSerializer,
    PasswordResetSerializer,
    PasswordResetConfirmSerializer
)
from .utils import send_verification_email

User = get_user_model()

class RegisterStudentView(generics.CreateAPIView):
    serializer_class = StudentRegistrationSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        user = serializer.save(role='student')
        send_verification_email(user, self.request)

class RegisterLecturerView(generics.CreateAPIView):
    serializer_class = LecturerRegistrationSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        user = serializer.save(role='lecturer')
        send_verification_email(user, self.request)

class RegisterRegistrarView(generics.CreateAPIView):
    serializer_class = RegistrarRegistrationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        user = serializer.save(role='registrar')
        user.is_verified = True
        user.save()

class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        if not email or not password:
            return Response({'error': 'Email and password are required'}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.filter(email=email).first()

        if user is None or not user.is_verified:
            return Response({'error': 'Invalid email or password'}, status=status.HTTP_401_UNAUTHORIZED)

        user = authenticate(request, username=email, password=password)
        if user is None:
            return Response({'error': 'Invalid email or password'}, status=status.HTTP_401_UNAUTHORIZED)

        refresh = RefreshToken.for_user(user)
        return Response({
            'access_token': str(refresh.access_token),
            'refresh_token': str(refresh),
            'role': user.role,
            'is_verified': user.is_verified,
        }, status=status.HTTP_200_OK)

class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data.get('refresh_token')
            if not refresh_token:
                return Response({'error': 'Refresh token is required'}, status=status.HTTP_400_BAD_REQUEST)
            
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({'message': 'Logout successful'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class PasswordResetRequestView(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = PasswordResetSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            user = User.objects.filter(email=email).first()
            if user:
                token = default_token_generator.make_token(user)
                uid = urlsafe_base64_encode(force_bytes(user.pk))
                reset_link = f"{settings.FRONTEND_URL}/password-reset/{uid}/{token}/"

                send_mail(
                    'Password Reset Request',
                    f'Click the link to reset your password: {reset_link}',
                    settings.DEFAULT_FROM_EMAIL,
                    [email],
                    fail_silently=False,
                )

            return Response({'message': 'If the email exists, a reset link has been sent.'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PasswordResetConfirmView(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = PasswordResetConfirmSerializer

    def post(self, request, uidb64, token):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
            if not default_token_generator.check_token(user, token):
                return Response({'error': 'Invalid or expired token'}, status=status.HTTP_400_BAD_REQUEST)

            user.set_password(serializer.validated_data['new_password'])
            user.save()
            return Response({'message': 'Password has been reset successfully'}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


User = get_user_model()

class VerifyEmailView(views.APIView):
    """Handles email verification"""

    def get(self, request, token):
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            user = get_object_or_404(User, id=payload["user_id"])

            if user.is_verified:
                return Response({"message": "Email already verified"}, status=status.HTTP_200_OK)

            user.is_verified = True
            user.save()

            return Response({"message": "Email successfully verified"}, status=status.HTTP_200_OK)

        except jwt.ExpiredSignatureError:
            return Response({"error": "Verification link has expired"}, status=status.HTTP_400_BAD_REQUEST)
        except jwt.DecodeError:
            return Response({"error": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST)

class ResendVerificationEmailView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        """Resend verification email"""
        serializer = ResendVerificationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            user.generate_new_verification_token()
            send_verification_email(user, request)
            return Response(
                {'message': 'Verification email resent successfully'},
                status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)