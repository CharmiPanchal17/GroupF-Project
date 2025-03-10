from django.db import models

# Create your models here.
class Issue(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=50, choices=[('open', 'Open'), ('closed', 'Closed')])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title