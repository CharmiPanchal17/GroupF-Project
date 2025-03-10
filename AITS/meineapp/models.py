from django.db import models

# Create your models here.
class Student(models.Model):
    Username = models.CharField(max_length=100)