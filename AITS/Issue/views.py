from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Issue
from .serializers import IssueSerializer

class IssueViewSet(viewsets.ModelViewSet):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import Issue, Assignment, Notification
from .serializers import IssueSerializer, AssignmentSerializer, NotificationSerializer

# Get all issues or create a new one
@api_view(['GET', 'POST'])
@permission_classes([permissions.IsAuthenticated])
def issue_list(request):
    if request.method == 'GET':
        issues = Issue.objects.all()
        serializer = IssueSerializer(issues, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = IssueSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(student=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Get, update, or delete an issue
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([permissions.IsAuthenticated])
def issue_detail(request, pk):
    try:
        issue = Issue.objects.get(pk=pk)
    except Issue.DoesNotExist:
        return Response({'error': 'Issue not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = IssueSerializer(issue)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = IssueSerializer(issue, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        issue.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Assign an issue to a lecturer
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def assign_issue(request):
    serializer = AssignmentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(registrar=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Fetch notifications for a user
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def user_notifications(request):
    notifications = Notification.objects.filter(recipient=request.user)
    serializer = NotificationSerializer(notifications, many=True)
    return Response(serializer.data)




@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def student_dashboard(request):
    issues = Issue.objects.filter(student=request.user)
    serializer = IssueSerializer(issues, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def lecturer_dashboard(request):
    assignments = Assignment.objects.filter(lecturer=request.user)
    data = [{'issue': a.issue.title, 'status': a.issue.status} for a in assignments]
    return Response(data)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def registrar_dashboard(request):
    issues = Issue.objects.all()
    serializer = IssueSerializer(issues, many=True)
    return Response(serializer.data)
