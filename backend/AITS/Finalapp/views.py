from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from .models import CustomUser, Issue, Assignment, Notification
from .serializers import UserSerializer, IssueSerializer, AssignmentSerializer, NotificationSerializer

# User Registration View
@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    data = request.data
    data['password'] = make_password(data['password'])  # Hash password
    serializer = UserSerializer(data=data)
    
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "User registered successfully!"}, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# User Login View
@api_view(['POST'])
@permission_classes([AllowAny])
def login_user(request):
    username = request.data.get("username")
    password = request.data.get("password")
    user = authenticate(username=username, password=password)
    
    if user:
        return Response({"message": "Login successful!", "user": UserSerializer(user).data})
    
    return Response({"message": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

# Submit Issue (Students Only)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def submit_issue(request):
    if request.user.role != 'student':
        return Response({"error": "Only students can submit issues!"}, status=status.HTTP_403_FORBIDDEN)

    serializer = IssueSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(student=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Assign Issue to Lecturer (Registrar Only)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def assign_issue(request, issue_id):
    if request.user.role != 'registrar':
        return Response({"error": "Only registrar can assign issues!"}, status=status.HTTP_403_FORBIDDEN)

    issue = get_object_or_404(Issue, id=issue_id)
    lecturer = get_object_or_404(CustomUser, id=request.data.get('lecturer_id'), role='lecturer')

    assignment = Assignment.objects.create(issue=issue, registrar=request.user, lecturer=lecturer)
    issue.status = "assigned"
    issue.save()

    # Create notification
    Notification.objects.create(recipient=lecturer, message=f"You have been assigned issue '{issue.title}'")

    return Response(AssignmentSerializer(assignment).data, status=status.HTTP_201_CREATED)

# View Student Dashboard (Student Issues)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def student_dashboard(request):
    if request.user.role != 'student':
        return Response({"error": "Access denied"}, status=status.HTTP_403_FORBIDDEN)

    issues = Issue.objects.filter(student=request.user)
    return Response(IssueSerializer(issues, many=True).data)

# View Lecturer Dashboard (Assigned Issues)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def lecturer_dashboard(request):
    if request.user.role != 'lecturer':
        return Response({"error": "Access denied"}, status=status.HTTP_403_FORBIDDEN)

    assignments = Assignment.objects.filter(lecturer=request.user)
    return Response(AssignmentSerializer(assignments, many=True).data)

# View Registrar Dashboard (All Issues & Assignments)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def registrar_dashboard(request):
    if request.user.role != 'registrar':
        return Response({"error": "Access denied"}, status=status.HTTP_403_FORBIDDEN)

    issues = Issue.objects.all()
    assignments = Assignment.objects.all()

    return Response({
        "all_issues": IssueSerializer(issues, many=True).data,
        "all_assignments": AssignmentSerializer(assignments, many=True).data,
    })

# Get User Notifications
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_notifications(request):
    notifications = Notification.objects.filter(recipient=request.user)
    return Response(NotificationSerializer(notifications, many=True).data)
