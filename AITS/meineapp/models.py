from django.db import models

# Create your models here.
class Student(models.Model):
    Username = models.CharField(max_length=100)

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    USER_TYPES = (
        ('student', 'Student'),
        ('lecturer', 'Lecturer'),
        ('registrar', 'Registrar'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPES, default='student')

    def __str__(self):
        return f"{self.username} ({self.user_type})"


class Issue(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('assigned', 'Assigned'),
        ('resolved', 'Resolved'),
    )

    student = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='issues', limit_choices_to={'user_type': 'student'})
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Assignment(models.Model):
    issue = models.OneToOneField(Issue, on_delete=models.CASCADE, related_name='assignment')
    registrar = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='assigned_issues', limit_choices_to={'user_type': 'registrar'})
    lecturer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='assigned_lectures', limit_choices_to={'user_type': 'lecturer'})
    assigned_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Issue '{self.issue.title}' assigned to {self.lecturer.username}"


class Notification(models.Model):
    recipient = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='notifications')
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification for {self.recipient.username}"
