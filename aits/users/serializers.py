from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'role','password', 'student_number', 'registration_number', 'lecturer_reg_number',]

    extra_kwargs = {
        'password': {'write_only': True},
        'id': {'read_only': True},
        'student_number': {'required': False},
        'registration_number': {'required': False},
        'lecturer_reg_number': {'required': False},
    }

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
    
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create_user(email=validated_data['email'], password=password, **validated_data)
        return user
    
    def validate(self, data):
        role = data.get('role')
        if role == 'student'and not data.get('student_number'):
            raise serializers.ValidationError('Student number is required for students')
        elif role == 'lecturer' and not data.get('lecturer_reg_number'):
            raise serializers.ValidationError('Lecturer registration number is required for lecturers')
        elif role == 'registrar' and not data.get('registration_number'):
            raise serializers.ValidationError('Registration number is required for registrars')
        

        if role != 'student':
            data['student_number'] = None
        if role != 'lecturer':
            data['lecturer_reg_number'] = None
        if role != 'registrar':
            data['registration_number'] = None
        return data
    
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = User(UserSerializer.Meta)
        fields = ['id', 'email', 'first_name', 'last_name', 'password' ,'role', 'student_number']
    def validate(self, data):
        data['role'] = 'student'
        return super().validate(data)
    
class LecturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User(UserSerializer.Meta)
        fields = ['id', 'email', 'first_name', 'last_name', 'password' ,'role', 'lecturer_reg_number']
    def validate(self, data):
        data['role'] = 'lecturer'
        return super().validate(data)
    
class RegistrarSerializer(serializers.ModelSerializer):
    class Meta:
        model = User(UserSerializer.Meta)
        fields = ['id', 'email', 'first_name', 'last_name', 'password' ,'role', 'registration_number']
    def validate(self, data):
        data['role'] = 'registrar'
        return super().validate(data)
    
        
            

        
