from rest_framework import viewsets, permissions, generics
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from issues.views import IsRegistrar
from .serializers import  StudentSerializer, LecturerSerializer, RegistrarSerializer, UserSerializer, LecturerListSerializer
from .models import User

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

        return Response({
            'access_token': access_token,
            'refresh_token': str(refresh),
            'role': user.role,
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