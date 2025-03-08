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

# CREATING USER
@api_view(['POST'])
def create_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#LISTING USERS - Fetching only necessary fields
@api_view(['GET'])
def list_users(request):
    users = User.objects.only('id', 'username', 'role', 'email')  # Optimized
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

# CREATING A STUDENT
@api_view(['POST'])
def create_student(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# LISTING STUDENTS 
@api_view(['GET'])
def list_students(request):
    students = Student.objects.select_related('user').all()  # Optimized with select_related
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)

# CREATING LECTURER
@api_view(['POST'])
def create_lecturer(request):
    serializer = LecturerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# LISTING LECTURERS
@api_view(['GET'])
def list_lecturers(request):
    lecturers = Lecturer.objects.select_related('user').all()
    serializer = LecturerSerializer(lecturers, many=True)
    return Response(serializer.data)

# CREATING REGISTRAR
@api_view(['POST'])
def create_registrar(request):
    serializer = RegistrarSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# LISTING REGISTRARS
@api_view(['GET'])
def list_registrars(request):
    registrars = Registrar.objects.select_related('user').all()
    serializer = RegistrarSerializer(registrars, many=True)
    return Response(serializer.data)

# CREATING AN ISSUE BY Students only
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

# LISTING ISSUES
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_issues(request):
    """Filter issues based on user role"""
    if request.user.role == 'student':
        issues = Issue.objects.filter(submitted_by=request.user).only('id', 'category', 'status', 'assigned_to')
    elif request.user.role == 'lecturer':
        issues = Issue.objects.filter(assigned_to=request.user).only('id', 'category', 'status', 'submitted_by')
    elif request.user.role == 'registrar':
        issues = Issue.objects.only('id', 'category', 'status', 'assigned_to', 'submitted_by')
    else:
        return Response({"error": "Invalid role"}, status=status.HTTP_403_FORBIDDEN)

    serializer = IssueSerializer(issues, many=True)
    return Response(serializer.data)

# ASSIGNING ISSUE 
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def assign_issue(request, issue_id, lecturer_id):
    if request.user.role != 'registrar':
        return Response({"error": "Only registrars can assign issues."}, status=status.HTTP_403_FORBIDDEN)

    try:
        issue = Issue.objects.get(id=issue_id, status='open')  # Fetch only open issues
        lecturer = User.objects.get(id=lecturer_id, role='lecturer')
    except Issue.DoesNotExist:
        return Response({"error": "Issue not found or already assigned."}, status=status.HTTP_404_NOT_FOUND)
    except User.DoesNotExist:
        return Response({"error": "Lecturer not found."}, status=status.HTTP_404_NOT_FOUND)

    issue.assigned_to = lecturer
    issue.status = 'in_progress'
    issue.save()
    
    return Response({"message": f"Issue {issue_id} assigned to {lecturer.username}."}, status=status.HTTP_200_OK)

# RESOLVING ISSUE 
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def resolve_issue(request, issue_id):
    if request.user.role != 'lecturer':
        return Response({"error": "Only lecturers can resolve issues."}, status=status.HTTP_403_FORBIDDEN)

    try:
        issue = Issue.objects.get(id=issue_id, assigned_to=request.user, status='in_progress')  # Fetch only in-progress issues
    except Issue.DoesNotExist:
        return Response({"error": "Issue not found or not assigned to you."}, status=status.HTTP_404_NOT_FOUND)

    issue.status = 'resolved'
    issue.resolved_at = timezone.now()
    issue.save()

    return Response({"message": f"Issue {issue_id} resolved."}, status=status.HTTP_200_OK)

# LISTING NOTIFICATIONS
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_notifications(request):
    """Return only unread notifications for a user"""
    notifications = Notification.objects.filter(user=request.user).only('message', 'created_at')
    serializer = NotificationSerializer(notifications, many=True)
    return Response(serializer.data)
