from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Custom UserManager to handle email as the USERNAME_FIELD
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

# Create your models here
class User(AbstractUser):
    ROLES = (
        ('student', 'Student'),
        ('lecturer', 'Lecturer'),
        ('registrar', 'Registrar'),
    )
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=20, choices=ROLES, default='student')
    student_number = models.CharField(max_length=50, unique=True, blank=True, null=True)  # Fixed typo: "nunmber" to "number"
    registration_number = models.CharField(max_length=50, unique=True, blank=True, null=True)
    lecturer_reg_number = models.CharField(max_length=50, unique=True, blank=True, null=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    # Assign the custom UserManager
    objects = UserManager()

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups',
        blank=True,
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',
        blank=True,
    )
    
    def __str__(self):
        return self.email