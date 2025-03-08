from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Student, Lecturer, Registrar, Issue, Notification

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role']

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'user', 'student_id', 'year', 'course']

class LecturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecturer
        fields = ['id', 'user', 'department', 'specialization']

class RegistrarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registrar
        fields = ['id', 'user', 'office_location']

class IssueSerializer(serializers.ModelSerializer): #Automatically includes submitted_by and assigned_to relationships
    submitted_by = serializers.StringRelatedField(read_only=True)
    assigned_to = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Issue
        fields = ['id', 'category', 'description', 'status', 'submitted_by', 'assigned_to', 'created_at', 'resolved_at']

class NotificationSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = Notification
        fields = ['id', 'user', 'message', 'created_at']



        
