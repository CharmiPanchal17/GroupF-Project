from rest_framework import serializers
from .models import CustomUser, Issue, Assignment, Notification

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'role']

# Issue Serializer
class IssueSerializer(serializers.ModelSerializer):
    student = UserSerializer(read_only=True)

    class Meta:
        model = Issue
        fields = ['id', 'title', 'description', 'status', 'student', 'created_at']

# Assignment Serializer
class AssignmentSerializer(serializers.ModelSerializer):
    issue = IssueSerializer(read_only=True)
    registrar = UserSerializer(read_only=True)
    lecturer = UserSerializer(read_only=True)

    class Meta:
        model = Assignment
        fields = ['id', 'issue', 'registrar', 'lecturer', 'assigned_at']

# Notification Serializer
class NotificationSerializer(serializers.ModelSerializer):
    recipient = UserSerializer(read_only=True)

    class Meta:
        model = Notification
        fields = ['id', 'recipient', 'message', 'created_at']
