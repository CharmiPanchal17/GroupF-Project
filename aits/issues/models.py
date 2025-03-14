from django.db import models
from users.models import User

# Create your models here.
class Issue(models.Model):
    STATUS_CHOICES = (
        ('open' , 'Open'),
        ('pending' , 'Pending'),
        ('resolved' , 'Resolved'),
    )
    title = models.CharField(max_length=200)
    description = models.TextField()
    submitted_by = models.ForeignKey(User,on_delete=models.CASCADE, related_name='issues_submitted')
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='issues_assigned', null =True, limit_choices_to={'role':'lecturer'})
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=25, default='open')

    def __str__(self):
        return self.title
 