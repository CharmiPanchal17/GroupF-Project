from rest_framework import serializers
from .models import RegisteredStudent

# class IssueSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Issue
#         fields = '__all__'

class RegisteredStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegisteredStudent
        fields = '__all__'

        
