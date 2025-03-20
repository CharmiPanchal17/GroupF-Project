# users/models.py
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone
from django.db import models

# Predefined registrar emails for validation
REGISTRAR_EMAILS = ["registrar1@mak.ac.ug", "registrar2@mak.ac.ug"] 

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        
        # Auto-assign role
        extra_fields["role"] = self.determine_role(email)
        
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
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

    email = models.EmailField(unique=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def send_notification(self, recipient, message):
        """Helper function to send a notification."""
        Notification.objects.create(user=recipient, message=message)

    def submit_issue(self, category, description):
        if self.role != 'student':
            raise PermissionError("Only students can submit issues.")
        
        issue = Issue.objects.create(
            category=category,
            status='pending',
            description=description,
            submitted_by=self
        )

        # Notifying the registrars
        registrars = User.objects.filter(role='registrar')
        for registrar in registrars:
            self.send_notification(registrar, f"New issue submitted: {category} by {self.email}.")

        return issue

    def assign_issue(self, issue, lecturer):
        if self.role != 'registrar':
            raise PermissionError("Only Registrar can assign issues to lecturers")
        if lecturer.role != 'lecturer':
            raise ValueError("Issues can only be assigned to lecturers")
        issue.assigned_to = lecturer
        issue.status = 'in_progress'
        issue.save()
        self.send_notification(lecturer, f"You have been assigned Issue {issue.id}: {issue.category}.")
        self.send_notification(issue.submitted_by, f"Your issue '{issue.category}' has been assigned to {lecturer.email}.")


    def resolve_issue(self, issue):
        if self.role != 'lecturer':
            raise PermissionError("Only lecturers can resolve issues")
        if issue.assigned_to != self:
            raise PermissionError("You can only resolve issues assigned to you")
        issue.status = 'resolved'
        issue.resolved_at = timezone.now()
        issue.save()
        self.send_notification(issue.submitted_by, f"Your issue '{issue.category}' has been resolved.")


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
        return f"{self.user.username} - {self.course}"

class Department(models.Model):
    department_id=models.IntegerField(primary_key=True)
    name= models.CharField(max_length=100)


class Lecturer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='lecturer')
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=False, blank=True, related_name='lecturers') 

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
        return f"Notification for {self.user.username}: {self.message}"