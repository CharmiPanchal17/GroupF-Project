from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from .models import Student, Lecturer, Registrar, Issue, Notification
from .serializers import (
    UserSerializer, StudentSerializer, LecturerSerializer,
    RegistrarSerializer, IssueSerializer, NotificationSerializer
)
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone


User = get_user_model()

@api_view(['POST'])
def create_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def list_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_student(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def list_students(request):
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_lecturer(request):
    serializer = LecturerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def list_lecturers(request):
    lecturers = Lecturer.objects.all()
    serializer = LecturerSerializer(lecturers, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_registrar(request):
    serializer = RegistrarSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def list_registrars(request):
    registrars = Registrar.objects.all()
    serializer = RegistrarSerializer(registrars, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_issue(request):
    if request.user.role != 'student':
        return Response({"error": "Only students can submit issues."}, status=status.HTTP_403_FORBIDDEN)
    
    serializer = IssueSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(submitted_by=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_issues(request):
    issues = Issue.objects.all()
    serializer = IssueSerializer(issues, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def assign_issue(request, issue_id, lecturer_id):
    if request.user.role != 'registrar':
        return Response({"error": "Only registrars can assign issues."}, status=status.HTTP_403_FORBIDDEN)

    try:
        issue = Issue.objects.get(id=issue_id)
        lecturer = User.objects.get(id=lecturer_id, role='lecturer')
    except Issue.DoesNotExist:
        return Response({"error": "Issue not found."}, status=status.HTTP_404_NOT_FOUND)
    except User.DoesNotExist:
        return Response({"error": "Lecturer not found."}, status=status.HTTP_404_NOT_FOUND)

    issue.assigned_to = lecturer
    issue.status = 'in_progress'
    issue.save()
    
    return Response({"message": f"Issue {issue_id} assigned to {lecturer.username}."}, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def resolve_issue(request, issue_id):
    if request.user.role != 'lecturer':
        return Response({"error": "Only lecturers can resolve issues."}, status=status.HTTP_403_FORBIDDEN)

    try:
        issue = Issue.objects.get(id=issue_id)
    except Issue.DoesNotExist:
        return Response({"error": "Issue not found."}, status=status.HTTP_404_NOT_FOUND)

    if issue.assigned_to != request.user:
        return Response({"error": "You can only resolve issues assigned to you."}, status=status.HTTP_403_FORBIDDEN)

    issue.status = 'resolved'
    issue.resolved_at = timezone.now()
    issue.save()

    return Response({"message": f"Issue {issue_id} resolved."}, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_notifications(request):
    notifications = Notification.objects.filter(user=request.user)
    serializer = NotificationSerializer(notifications, many=True)
    return Response(serializer.data)

