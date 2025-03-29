from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.validators import RegexValidator
from django.utils import timezone
import uuid
from django.core.mail import send_mail

# Predefined registrar emails for validation
REGISTRAR_EMAILS = ["registrar1@mak.ac.ug", "registrar2@mak.ac.ug"]

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)

        # Auto-assign role
        extra_fields["role"] = self.determine_role(email)
        extra_fields.setdefault('is_verified', False)  # Default to not verified

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        # Send verification email
        user.send_verification_email()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_verified", True)
        return self.create_user(email, password, **extra_fields)

    def determine_role(self, email):
        """Assign user role based on email domain."""
        email_domain = email.split('@')[-1].lower()

        if email_domain == "students.mak.ac.ug":
            return "student"
        elif email in REGISTRAR_EMAILS:
            return "registrar"
        elif email_domain == "mak.ac.ug":
            return "lecturer"
        else:
            raise ValueError("Invalid email domain for user role assignment.")

class User(AbstractBaseUser, PermissionsMixin):
    ROLE_CHOICES = [
        ('student', 'Student'),
        ('lecturer', 'Lecturer'),
        ('registrar', 'Registrar'),
    ]

    number_validator = RegexValidator(
        regex=r'^[A-Za-z0-9-]+$',
        message='Only alphanumeric characters and hyphens are allowed',
    )

    email = models.EmailField(unique=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    verification_token = models.UUIDField(default=uuid.uuid4, editable=False)
    token_created_at = models.DateTimeField(default=timezone.now)

    student_no = models.CharField(max_length=50, unique=True, blank=True, null=True, validators=[number_validator])
    registration_number = models.CharField(max_length=50, unique=True, blank=True, null=True, validators=[number_validator])

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def generate_new_verification_token(self):
        """Generates a new email verification token"""
        self.verification_token = uuid.uuid4()
        self.token_created_at = timezone.now()
        self.save()
        return self.verification_token

    def send_verification_email(self):
        """Sends verification email to user"""
        subject = "Verify Your Email Address"
        message = f"Click the link to verify your account: http://yourdomain.com/verify/{self.verification_token}/"
        send_mail(subject, message, "noreply@yourdomain.com", [self.email])

    def save(self, *args, **kwargs):
        """Override save to send verification email when a new user is created"""
        new_user = self.pk is None
        super().save(*args, **kwargs)
        if new_user and not self.is_verified:
            self.send_verification_email()

    def __str__(self):
        return f"{self.email} ({self.get_role_display()})"

class Student(models.Model):
    YEAR_CHOICES = [
        (1, 'Year 1'),
        (2, 'Year 2'),
        (3, 'Year 3'),
        (4, 'Year 4'),
    ]
    
    COURSE_CHOICES = [
        ('cs', 'Computer Science'),
        ('se', 'Software Engineering'),
        ('it', 'Information Technology and Sciences'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student')
    student_no = models.CharField(max_length=50, unique=True)
    year = models.IntegerField(choices=YEAR_CHOICES)
    course = models.CharField(max_length=50, choices=COURSE_CHOICES)

    def __str__(self):
        return f"{self.user.email} - {self.course}"

class Department(models.Model):
    department_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)

class Lecturer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='lecturer')
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True, related_name='lecturers')

class Registrar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='registrar')
    college = models.CharField(max_length=100)

class Issue(models.Model):
    STATUS_CHOICES = [
        ('pending', 'pending'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
    ]
    
    category = models.CharField(max_length=100)  
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending') 
    description = models.TextField()  
    submitted_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="submitted_issues", limit_choices_to={"role": "student"})  
    assigned_to = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name="assigned_issues", limit_choices_to={"role": "lecturer"}) 
    created_at = models.DateTimeField(auto_now_add=True) 
    resolved_at = models.DateTimeField(null=True, blank=True)    
    
    def __str__(self):
        return f"Issue {self.id} - {self.category} ({self.status})"

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    message = models.TextField()  
    created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return f"Notification for {self.user.email}: {self.message}"
