from django.shortcuts import render
from .models import Student
# Create your views here.
def home(request):
    return render(request,"base.html")

def student(request):
    items = Student.objects.all()
    return render(request, 'login.html', {'student':items})

from rest_framework import viewsets, permissions
from .models import Issue, Assignment, Notification
from .serializers import IssueSerializer, AssignmentSerializer, NotificationSerializer
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

class IssueViewSet(viewsets.ModelViewSet):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(student=self.request.user)


class AssignmentViewSet(viewsets.ModelViewSet):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer
    permission_classes = [permissions.IsAuthenticated]


class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]
