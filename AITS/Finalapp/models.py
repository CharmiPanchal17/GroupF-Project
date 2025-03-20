from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

# Custom User Model
class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('student', 'Student'),
        ('lecturer', 'Lecturer'),
        ('registrar', 'Registrar'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='student')
    
    REGISTRAR_EMAILS = ["registrar1@mak.ac.ug", "registrar2@mak.ac.ug"]  # Add actual registrar emails

    def save(self, *args, **kwargs):
        email_domain = self.email.split('@')[-1].lower()
        if email_domain == "students.mak.ac.ug":
           self.user_type = "student"
        elif self.email.lower() in REGISTRAR_EMAILS:
           self.user_type = "registrar"
        elif email_domain == "mak.ac.ug":
         self.user_type = "lecturer"
        else:
         raise ValueError("Invalid email domain.")
    
        super().save(*args ,**kwargs)


    def __str__(self):
        return f"{self.username} ({self.role})"

# Student Profile Model
class StudentProfile(models.Model):

    # Define choices for year
    YEAR_CHOICES = [
        ('1', 'First Year'),
        ('2', 'Second Year'),
        ('3', 'Third Year'),
        ('4', 'Fourth Year'),
    ]

    # Define choices for course
    COURSE_CHOICES = [
        ('cs', 'Computer Science'),
        ('Li', ' Library and Information Technology'),
        ('se', 'Software Engineering'),
    ]

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='student_profile')
    student_id = models.CharField(max_length=50, unique=True)
    college = models.CharField(max_length=100)
    course = models.CharField(max_length=2, choices=COURSE_CHOICES, default='cs') 
    year_level = models.CharField(max_length=1, choices=YEAR_CHOICES, default='1')

    def __str__(self):
        return f"{self.user.username} - {self.department}"

# Lecturer Profile Model
class LecturerProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='lecturer_profile')
    department = models.CharField(max_length=100)
    office_number = models.CharField(max_length=50)
    specialization = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user.username} ({self.specialization})"

# Registrar Profile Model
class RegistrarProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='registrar_profile')
    department = models.CharField(max_length=100)
    office_location = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user.username} - {self.department}"

# Issue Model
class Issue(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('assigned', 'Assigned'),
        ('resolved', 'Resolved'),
    )

    student = models.ForeignKey(
        CustomUser, 
        on_delete=models.CASCADE, 
        related_name='issues', 
        limit_choices_to={'role': 'student'}
    )
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Issue '{self.title}' ({self.status})"

# Assignment Model
class Assignment(models.Model):
    issue = models.OneToOneField(Issue, on_delete=models.CASCADE, related_name='assignment')
    registrar = models.ForeignKey(
        CustomUser, 
        on_delete=models.CASCADE, 
        related_name='registrar_assignments', 
        limit_choices_to={'role': 'registrar'}
    )
    lecturer = models.ForeignKey(
        CustomUser, 
        on_delete=models.CASCADE, 
        related_name='lecturer_assignments', 
        limit_choices_to={'role': 'lecturer'}
    )
    assigned_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Issue '{self.issue.title}' assigned to {self.lecturer.username}"

# Notification Model
class Notification(models.Model):
    recipient = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='notifications')
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification for {self.recipient.username}: {self.message}"
