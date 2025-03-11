from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.core.validators import RegexValidator

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, password, **extra_fields)

class User(AbstractUser):
    ROLES = (
        ('student', 'Student'),
        ('lecturer', 'Lecturer'),
        ('registrar', 'Registrar'),
    )

    number_validator = RegexValidator(
        regex=r'^[A-Za-z0-9-]+$',
        message='Only alphanumeric characters and hyphens are allowed',
    )

    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, blank=True, null=True, unique=True)
    role = models.CharField(max_length=20, choices=ROLES, default='student')
    student_number = models.CharField(max_length=50, unique=True, blank=True, null=True, validators=[number_validator]) 
    registration_number = models.CharField(max_length=50, unique=True, blank=True, null=True,validators=[number_validator])
    lecturer_reg_number = models.CharField(max_length=50, unique=True, blank=True, null=True, validators=[number_validator])
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = UserManager()

    class Meta:
        permissions = [
            ('log_issue','Can log an issue'),
            ('view_issue','Can view issues'),
            ('resolve_issue','Can resolve issues'),
            ('provide_feedback','Can provide feedback'),
            ('assign_issue','Can assign issues to lecturers'),
            ('oversee_issues','Can oversee all issues')
        ]
    def __str__(self):
        return f'{self.email}({self.get_role_display()})'
