from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone


from .models import Student, Lecturer, Registrar, Issue, Notification
from .serializers import (
    UserSerializer, StudentSerializer, LecturerSerializer, RegistrarSerializer,
    IssueSerializer, IssueCreateSerializer, NotificationSerializer
)

User = get_user_model()

# --- USER REGISTRATION & AUTHENTICATION ---

@api_view(['POST'])
def register_user(request):
    """Register a new user (Student, Lecturer, or Registrar)"""
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login_user(request):
    """Authenticate user and start session"""
    email = request.data.get('email')
    password = request.data.get('password')
    user = authenticate(request, email=email, password=password)
    if user:
        login(request, user)
        return Response({"message": "Login successful"}, status=status.HTTP_200_OK)
    return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)


# --- ISSUE MANAGEMENT ---

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def submit_issue(request):
    """Allow students to submit issues"""
    if request.user.role != 'student':
        return Response({"error": "Only students can submit issues."}, status=status.HTTP_403_FORBIDDEN)
    
    serializer = IssueCreateSerializer(data=request.data)
    if serializer.is_valid():
        issue = serializer.save(submitted_by=request.user)
        return Response(IssueSerializer(issue).data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def assign_issue(request, issue_id):
    """Allow registrars to assign issues to lecturers"""
    if request.user.role != 'registrar':
        return Response({"error": "Only registrars can assign issues."}, status=status.HTTP_403_FORBIDDEN)

    try:
        issue = Issue.objects.get(id=issue_id)
        lecturer_id = request.data.get('lecturer_id')
        lecturer = User.objects.get(id=lecturer_id, role='lecturer')
        issue.assigned_to = lecturer
        issue.status = 'in_progress'
        issue.save()
        return Response(IssueSerializer(issue).data, status=status.HTTP_200_OK)
    except Issue.DoesNotExist:
        return Response({"error": "Issue not found."}, status=status.HTTP_404_NOT_FOUND)
    except User.DoesNotExist:
        return Response({"error": "Lecturer not found."}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def resolve_issue(request, issue_id):
    """Allow assigned lecturers to resolve issues"""
    if request.user.role != 'lecturer':
        return Response({"error": "Only lecturers can resolve issues."}, status=status.HTTP_403_FORBIDDEN)

    try:
        issue = Issue.objects.get(id=issue_id)
        if issue.assigned_to != request.user:
            return Response({"error": "You can only resolve issues assigned to you."}, status=status.HTTP_403_FORBIDDEN)

        issue.status = 'resolved'
        issue.resolved_at = timezone.now()
        issue.save()
        return Response(IssueSerializer(issue).data, status=status.HTTP_200_OK)
    except Issue.DoesNotExist:
        return Response({"error": "Issue not found."}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_issues(request):
    """Retrieve all issues"""
    issues = Issue.objects.all()
    serializer = IssueSerializer(issues, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


# --- NOTIFICATIONS ---

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_notifications(request):
    """Retrieve user notifications"""
    notifications = Notification.objects.filter(user=request.user)
    serializer = NotificationSerializer(notifications, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
