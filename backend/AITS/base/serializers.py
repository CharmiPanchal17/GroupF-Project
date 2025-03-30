from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
import jwt
from django.conf import settings
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str

User = get_user_model()

class BaseRegistrationSerializer(serializers.ModelSerializer):
    """Base serializer for user registration with common fields."""
    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'first_name', 'last_name']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            username=validated_data.get('username'),
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            role=validated_data.get('role', 'student')
        )
        return user

class StudentRegistrationSerializer(BaseRegistrationSerializer):
    student_number = serializers.CharField(required=True)

    class Meta(BaseRegistrationSerializer.Meta):
        fields = BaseRegistrationSerializer.Meta.fields + ['student_number']

    def validate(self, data):
        data = super().validate(data)
        if not data.get('student_number'):
            raise serializers.ValidationError({"student_number": "This field is required for students."})
        return data

    def create(self, validated_data):
        validated_data['role'] = 'student'
        return super().create(validated_data)

class LecturerRegistrationSerializer(BaseRegistrationSerializer):
    lecturer_reg_number = serializers.CharField(required=True)

    class Meta(BaseRegistrationSerializer.Meta):
        fields = BaseRegistrationSerializer.Meta.fields + ['lecturer_reg_number']

    def validate(self, data):
        data = super().validate(data)
        if not data.get('lecturer_reg_number'):
            raise serializers.ValidationError({"lecturer_reg_number": "This field is required for lecturers."})
        return data

    def create(self, validated_data):
        validated_data['role'] = 'lecturer'
        return super().create(validated_data)

class RegistrarRegistrationSerializer(BaseRegistrationSerializer):
    def create(self, validated_data):
        validated_data['role'] = 'registrar'
        return super().create(validated_data)

class VerificationSerializer(serializers.Serializer):
    token = serializers.CharField()

    def validate(self, data):
        token = data['token']
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            user_id = payload['user_id']
            user = User.objects.get(id=user_id)

            if user.is_verified:
                raise serializers.ValidationError("Email is already verified.")

            data['user'] = user
            return data

        except jwt.ExpiredSignatureError:
            raise serializers.ValidationError("Verification link has expired.")
        except (jwt.InvalidTokenError, User.DoesNotExist):
            raise serializers.ValidationError("Invalid verification token.")

class ResendVerificationSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate(self, data):
        try:
            user = User.objects.get(email=data['email'])
            if user.is_verified:
                raise serializers.ValidationError("Email is already verified.")
            
            data['user'] = user
            return data
        except User.DoesNotExist:
            raise serializers.ValidationError("User with this email does not exist.")

class PasswordResetSerializer(serializers.Serializer):
    """Serializer for requesting password reset email"""
    email = serializers.EmailField()

    def validate_email(self, value):
        if not User.objects.filter(email=value).exists():
            raise serializers.ValidationError("No user found with this email.")
        return value

class PasswordResetConfirmSerializer(serializers.Serializer):
    """Serializer for resetting password"""
    new_password = serializers.CharField(write_only=True, min_length=8)
    confirm_password = serializers.CharField(write_only=True)

    def validate(self, data):
        if data['new_password'] != data['confirm_password']:
            raise serializers.ValidationError({"confirm_password": "Passwords do not match."})
        return data
