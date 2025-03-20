from rest_framework import viewsets, permissions, generics
from rest_framework.decorators import action
from.models import Issue
from django.urls import reverse
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from .serializers import IssueSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, BasePermission
from .views import IsRegistrar
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


class IsStudent(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'student'
    
class IsLecturer(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'lecturer'
    
class IsRegistrar(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'registrar'
    
class IssueViewSet(viewsets.ModelViewSet):
    serializer_class = IssueSerializer
    permission_classes = IsAuthenticated

    def get_queryset(self):
        user = self.request.user
        if user.has_perm('users.oversee_issues'):
            return Issue.objects.all()
        elif user.role == 'lecturer':
            return Issue.objects.filter(assigned_to=user)
        return Issue.objects.filter(created_by=user)
    
    def perform_create(self, serializer):
        if not self.request.user.has_perm('users.log_issue'):
            return Response({'error':'Permission_denied'}, status =status.HTTP_403_FORBIDDEN)
        serializer.save(created_by=self.request.user)

@action(detail=True, methods='post', permission_classes=[IsLecturer])
def resolve(self, request,pk=None):
    if not request.user.has_perm('users.resolve_issue'):
        return Response({'error':'Permission denied'}, status = status.HTTP_403_FORBIDDEN)
    issue = self.get_object()
    if issue.assigned_to != request.user:
        return Response({'error':'Not assigned to you'}, status = status.HTTP_403_FORBIDDEN)
    issue.status = 'resolved'
    issue.feedback = request.data.get('feedback')
    issue.save()
    return Response(IssueSerializer(issue).data)

@action(detail=True, methods='post', permission_classes=[IsRegistrar])
def assign(self, request,pk=None):
    if not request.user.has_perm('users.assign_issue'):
        return Response({'error':'Premission denied'}, status = status.HTTP_403_FORBIDDEN)
    issue = self.get_object()
    lecturer_id  = request.data.get('lecturer_id')
    try:
        lecturer = User.objects.get(id = lecturer_id, role='lecturer')
        issue.assigned_to = lecturer
        issue.status = 'in_progress'
        issue.save()
        return Response(IssueSerializer(issue).data)
    except User.DoesNotExist:
        return Response({'error':'Invalid_lecturer'}, status=status.HTTP_400_BAD_REQUEST)