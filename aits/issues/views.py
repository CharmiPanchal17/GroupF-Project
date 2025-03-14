from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, BasePermission
from .models import Issue
from .serializers import IssueSerializer
from users.models import User

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
