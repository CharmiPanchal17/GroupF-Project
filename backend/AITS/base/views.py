from rest_framework import permissions, generics
from django.urls import reverse
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, BasePermission
from .serializers import  StudentRegistrationSerializer, LecturerRegistrationSerializer, RegistrarRegistrationSerializer

class RegisterStudentView(generics.CreateAPIView):
    serializer_class = StudentRegistrationSerializer
    permission_classes = [permissions.AllowAny] 

class RegisterLecturerView(generics.CreateAPIView):
    serializer_class = LecturerRegistrationSerializer
    permission_classes = [permissions.AllowAny]
    
class RegisterRegistrarView(generics.CreateAPIView):
    serializer_class = RegistrarRegistrationSerializer
    permission_classes = [IsAuthenticated] 

class IsStudent(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'student'
    
class IsLecturer(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'lecturer'
    
class IsRegistrar(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'registrar'

class LoginView(APIView):
    permission_classes = []

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        if not email or not password:
            return Response({'error': 'Email and password are required'}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(request, username=email, password=password)

        if user is None:
            return Response({'error': 'Invalid email or password'}, status=status.HTTP_401_UNAUTHORIZED)

        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)

        if user.role == 'student':
            dashboard_url = reverse('base:student-dashboard')
        elif user.role == 'lecturer':
            dashboard_url = reverse('base:lecturer-dashboard')
        elif user.role == 'registrar':
            dashboard_url = reverse('base:registrar-dashboard')
        else:
            dashboard_url = None

        return Response({
            'access_token': access_token,
            'refresh_token': str(refresh),
            'role': user.role,
            'dashboard_url': dashboard_url,
        }, status=status.HTTP_200_OK)

class StudentDashboardView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if request.user.role != 'student':
            return Response({'error': 'You are not authorized to access this page'}, status=status.HTTP_403_FORBIDDEN)
        return Response({'message': 'Welcome to the Student Dashboard'})
    
class LecturerDashboardView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if request.user.role != 'lecturer':
            return Response({'error': 'You are not authorized to access this page'}, status=status.HTTP_403_FORBIDDEN)
        return Response({'message': 'Welcome to the Lecturer Dashboard'})
    
class RegistrarDashboardView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if request.user.role != 'registrar':
            return Response({'error': 'You are not authorized to access this page'}, status=status.HTTP_403_FORBIDDEN)
        return Response({'message': 'Welcome to the Registrar Dashboard'})
    
