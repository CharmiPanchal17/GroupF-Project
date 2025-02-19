from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Student(models.Model):
    username = models.CharField(max_length=100, unique=True)
    fullname = models.CharField(max_length=255)
    student_number = models.CharField(max_length=50, unique=True)
    registration_number = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255) 

    def __str__(self):
        return self.fullname

