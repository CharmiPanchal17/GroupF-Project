from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
import jwt
from django.conf import settings

User = get_user_model()

class BaseRegistrationSerializer(serializers.ModelSerializer):
    """
    Base serializer for user registration with common fields.
    """
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
            role=validated_data.get('role', 'student')  # Default role
        )
        return user

class StudentRegistrationSerializer(BaseRegistrationSerializer):
    """
    Serializer for student registration, requiring student_number.
    """
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
    """
    Serializer for lecturer registration, requiring lecturer_reg_number.
    """
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
    """
    Serializer for registrar registration (no additional fields required).
    """
    def create(self, validated_data):
        validated_data['role'] = 'registrar'
        return super().create(validated_data)

class VerificationSerializer(serializers.Serializer):
    """
    Serializer for email verification using JWT token.
    """
    token = serializers.CharField()

    def validate(self, data):
        token = data['token']
        try:
            # Decode JWT token
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            user_id = payload['user_id']
            user = User.objects.get(id=user_id)

            # Check if already verified
            if user.is_verified:
                raise ValidationError("Email is already verified.")

            # JWT expiration is handled by jwt.decode
            data['user'] = user
            return data

        except jwt.ExpiredSignatureError:
            raise ValidationError("Verification link has expired.")
        except (jwt.InvalidTokenError, User.DoesNotExist):
            raise ValidationError("Invalid verification token.")

class ResendVerificationSerializer(serializers.Serializer):

    email = serializers.EmailField()

    def validate(self, data):
        try:
            user = User.objects.get(email=data['email'])
            if user.is_verified:
                raise ValidationError("Email is already verified.")
            
            data['user'] = user  # Pass user object to the view
            return data
        except User.DoesNotExist:
            raise ValidationError("User with this email does not exist.")