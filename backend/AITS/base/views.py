from rest_framework import permissions, generics, status
from rest_framework.views import APIView
from django.contrib.auth import authenticate, get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from django.urls import reverse
from .serializers import (
    StudentRegistrationSerializer,
    LecturerRegistrationSerializer,
    RegistrarRegistrationSerializer,
    VerificationSerializer,
    ResendVerificationSerializer
)
from .utils import send_verification_email

User = get_user_model()

class RegisterStudentView(generics.CreateAPIView):
    serializer_class = StudentRegistrationSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        """Create a student & send verification email"""
        user = serializer.save(role='student')
        send_verification_email(user, self.request)

class RegisterLecturerView(generics.CreateAPIView):
    serializer_class = LecturerRegistrationSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        """Create a lecturer & send verification email"""
        user = serializer.save(role='lecturer')
        send_verification_email(user, self.request)

class RegisterRegistrarView(generics.CreateAPIView):
    serializer_class = RegistrarRegistrationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        """Create a registrar (requires authentication)"""
        user = serializer.save(role='registrar')
        user.is_verified = True
        user.save()

class VerifyEmailView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        """Verify user's email with a token"""
        serializer = VerificationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            user.is_verified = True
            user.verification_token = None
            user.save()
            return Response({'message': 'Email successfully verified'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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

class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        """Authenticate user and return JWT token"""
        email = request.data.get('email')
        password = request.data.get('password')

        if not email or not password:
            return Response({'error': 'Email and password are required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.filter(email=email).first()

            if user is None:
                return Response({'error': 'Invalid email or password'}, status=status.HTTP_401_UNAUTHORIZED)

            if not user.is_verified:
                return Response(
                    {
                        'error': 'Email not verified',
                        'resend_url': reverse('resend-verification'),
                        'email': user.email
                    },
                    status=status.HTTP_403_FORBIDDEN
                )

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

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
