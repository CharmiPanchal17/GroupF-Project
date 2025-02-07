from django.db import models

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