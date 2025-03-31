from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Student, Lecturer, Registrar, Issue, Notification, Department

User = get_user_model()

# USER SERIALIZER
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'role', 'password', 'is_verified', 'verification_token']
        extra_kwargs = {
            'password': {'write_only': True},
            'verification_token': {'read_only': True}
        }

    def create(self, validated_data):
        """Create user using CustomUserManager and return it."""
        return User.objects.create_user(**validated_data)

# STUDENT SERIALIZER
class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Student
        fields = ['user', 'student_no', 'year', 'course']

    def create(self, validated_data):
        """Handle nested user creation when creating a student."""
        user_data = validated_data.pop('user')
        user_data['role'] = 'student'  # Explicitly set role
        user = User.objects.create_user(**user_data)
        student = Student.objects.create(user=user, **validated_data)
        return student

# DEPARTMENT SERIALIZER
class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

# LECTURER SERIALIZER
class LecturerSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    department = serializers.PrimaryKeyRelatedField(queryset=Department.objects.all(), required=False)

    class Meta:
        model = Lecturer
        fields = ['user', 'department']

    def create(self, validated_data):
        """Handle nested user creation when creating a lecturer."""
        user_data = validated_data.pop('user')
        user_data['role'] = 'lecturer'  # Explicitly set role
        user = User.objects.create_user(**user_data)
        lecturer = Lecturer.objects.create(user=user, **validated_data)
        return lecturer

# REGISTRAR SERIALIZER
class RegistrarSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Registrar
        fields = ['user', 'college']

    def create(self, validated_data):
        """Handle nested user creation when creating a registrar."""
        user_data = validated_data.pop('user')
        user_data['role'] = 'registrar'  # Explicitly set role
        user = User.objects.create_user(**user_data)
        registrar = Registrar.objects.create(user=user, **validated_data)
        return registrar

# ISSUE SERIALIZER
class IssueSerializer(serializers.ModelSerializer):
    submitted_by = UserSerializer(read_only=True)
    assigned_to = UserSerializer(read_only=True)

    class Meta:
        model = Issue
        fields = ['id', 'category', 'status', 'description', 'submitted_by', 'assigned_to', 'created_at', 'resolved_at']
        read_only_fields = ['submitted_by', 'assigned_to', 'created_at', 'resolved_at']

# ISSUE CREATION SERIALIZER (For students to submit issues)
class IssueCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = ['category', 'description']

# NOTIFICATION SERIALIZER
class NotificationSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Notification
        fields = ['user', 'message', 'created_at']
        read_only_fields = ['created_at']
