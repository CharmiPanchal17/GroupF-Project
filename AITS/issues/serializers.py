from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Student, Lecturer, Registrar, Issue, Notification, Department

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'role', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            role=validated_data.get('role', 'student')
        )
        return user


class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Student
        fields = ['user', 'student_no', 'year', 'course']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create_user(**user_data, role='student')
        student = Student.objects.create(user=user, **validated_data)
        return student


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class LecturerSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    department = DepartmentSerializer()

    class Meta:
        model = Lecturer
        fields = ['user', 'department']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        department_data = validated_data.pop('department')
        user = User.objects.create_user(**user_data, role='lecturer')
        department, _ = Department.objects.get_or_create(**department_data)
        lecturer = Lecturer.objects.create(user=user, department=department)
        return lecturer


class RegistrarSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Registrar
        fields = ['user', 'college']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create_user(**user_data, role='registrar')
        registrar = Registrar.objects.create(user=user, **validated_data)
        return registrar


class IssueSerializer(serializers.ModelSerializer):
    submitted_by = serializers.StringRelatedField()
    assigned_to = serializers.StringRelatedField()

    class Meta:
        model = Issue
        fields = ['id', 'category', 'status', 'description', 'submitted_by', 'assigned_to', 'created_at', 'resolved_at']
        read_only_fields = ['submitted_by', 'created_at', 'resolved_at']


class IssueCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = ['category', 'description']


class NotificationSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = Notification
        fields = ['user', 'message', 'created_at']
