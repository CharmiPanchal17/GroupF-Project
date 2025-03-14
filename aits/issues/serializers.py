from rest_framework import serializers
from .models import Issue, User
from users.serializers import UserSerializer

class IssueSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only = True)
    assigned_to = UserSerializer(read_only = True)

    class Meta:
        model = Issue
        fields = '__all__'