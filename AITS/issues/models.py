from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Issue(models.Model):
    STATUS_CHOICES = [
        ('open', 'Open'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length= 20, choices= STATUS_CHOICES, default= 'open')
    created_at = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return self.title

class RegisteredStudent(models.Model):
    YEAR_CHOICES = [
        ('1', 'Year one'),
        ('2', 'Year two'),
        ('3', 'Year three'),
        ('4', 'Year four'),
    ]

    COURSE_CHOICES = [
        ('CS', 'Computer Science'),
        ('LI', 'Library and Information Technology'),
        ('SE', 'Software Engineering')
    ]

    name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=15, unique=True)
    year = models.CharField(max_length=1, choices=YEAR_CHOICES, default='1')
    course = models.CharField(max_length=2, choices= COURSE_CHOICES)
    issue = models.TextField()
    created_at = models.DateTimeField(auto_now_add= True)




