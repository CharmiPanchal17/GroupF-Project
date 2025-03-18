from rest_framework import viewsets, permissions, generics
from django.urls import reverse
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from issues.views import IsRegistrar
from .serializers import  StudentSerializer, LecturerSerializer, RegistrarSerializer, UserSerializer, LecturerListSerializer
from .models import User

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
    
class LoginView(APIView):
    permission_classes = []

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        role = request.data.get('role')

        user = authenticate(request, username=email, password=password)

        print(f"User: {user}")

        if user is None:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        if user.role != role:
            return Response({'error': f'You are not authorized to login as a {role}'}, status=status.HTTP_403_FORBIDDEN)

        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)

        if user.role == 'student':
            dashboard_url = reverse('users:student-dashboard')
        elif user.role == 'lecturer':
            dashboard_url = reverse('users:lecturer-dashboard')
        elif user.role == 'registrar':
            dashboard_url = reverse('users:registrar-dashboard')
        else:
            dashboard_url = None

        return Response({
            'access_token': access_token,
            'refresh_token': str(refresh),
            'role': user.role,
            'dashboard_url': dashboard_url, 
        }, status=status.HTTP_200_OK)

class LecturerViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = LecturerListSerializer
    permission_classes = [IsAuthenticated, IsRegistrar] 
    queryset = User.objects.filter(role='lecturer')

#students can register themselves since they are external users
class RegisterStudentView(generics.CreateAPIView):
    serializer_class = StudentSerializer
    permission_classes = [permissions.AllowAny] 

#registrar can register a lecturer
class RegisterLecturerView(generics.CreateAPIView):
    serializer_class = LecturerSerializer
    permission_classes = [IsAuthenticated, IsRegistrar] 

#registrars can register fellow registrars
class RegisterRegistrarView(generics.CreateAPIView):
    serializer_class = RegistrarSerializer
    permission_classes = [IsAuthenticated, IsRegistrar] 
