from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.core.validators import RegexValidator
import uuid
from django.utils import timezone
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        extra_fields.setdefault('is_verified', False)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_verified', True)
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
    is_staff = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    verification_token = models.UUIDField(default=uuid.uuid4, editable=False)
    token_created_at = models.DateTimeField(default=timezone.now)
    role = models.CharField(max_length=20, choices=ROLES, default='student')
    student_number = models.CharField(max_length=50, unique=True, blank=True, null=True, validators=[number_validator])
    registration_number = models.CharField(max_length=50, unique=True, blank=True, null=True, validators=[number_validator])
    lecturer_reg_number = models.CharField(max_length=50, unique=True, blank=True, null=True, validators=[number_validator])

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
    objects = UserManager()

    def generate_new_verification_token(self):
        """Generates a new email verification token"""
        self.verification_token = uuid.uuid4()
        self.token_created_at = timezone.now()
        self.save()
        return self.verification_token

    def send_verification_email(self, request=None):
        """Sends verification email to user"""
        from .utils import send_verification_email  
        send_verification_email(self, request)

    def save(self, *args, **kwargs):
        """Override save to send verification email when a new user is created"""
        new_user = self.pk is None 
        super().save(*args, **kwargs)
        if new_user and not self.is_verified: 
            self.send_verification_email()

    def __str__(self):
        return f'{self.email} ({self.get_role_display()})'
