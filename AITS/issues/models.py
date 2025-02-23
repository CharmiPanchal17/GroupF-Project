from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class User(AbstractUser):
    ROLE_CHOICES = [
        ('student', 'Student'),
        ('lecturer', 'Lecturer'),
        ('registrar', 'Registrar'),
    ]
    
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def submit_issue(self, category, description):
        """Allow only students to submit issues"""
        if self.role != 'student':
            raise PermissionError("Only students can submit issues.")
        
        issue = Issue.objects.create(
            category=category,
            description=description,
            submitted_by=self
        )
        
        Notification.create_notification(
            user=self,
            message=f"Issue submitted: {category}"
        )
        
        return issue

    def assign_issue(self, issue, lecturer):
        """Allow only registrars to assign issues to lecturers"""
        if self.role != 'registrar':
            raise PermissionError("Only registrars can assign issues.")
        
        if lecturer.role != 'lecturer':
            raise ValueError("Issue must be assigned to a lecturer.")
        
        issue.assigned_to = lecturer
        issue.status = 'in_progress'
        issue.save()

        Notification.create_notification(
            user=lecturer,
            message=f"New issue assigned: {issue.category}"
        )

    def resolve_issue(self, issue):
        """Allow only the assigned lecturer to resolve the issue"""
        if self.role != 'lecturer':
            raise PermissionError("Only lecturers can resolve issues.")
        
        if issue.assigned_to != self:
            raise PermissionError("You can only resolve issues assigned to you.")
        
        issue.status = 'resolved'
        issue.resolved_at = timezone.now()
        issue.save()

        Notification.create_notification(
            user=issue.submitted_by,
            message=f"Issue resolved: {issue.category}"
        )

# class Student(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student')
#     student_id = models.CharField(max_length=50, unique=True)
#     department = models.CharField(max_length=100)
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
    student_id = models.CharField(max_length=50, unique=True)
    year = models.IntegerField(choices=YEAR_CHOICES)
    course = models.CharField(max_length=50, choices=COURSE_CHOICES)

    def __str__(self):
        return f"{self.user.username} - {self.course}"

class Lecturer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='lecturer')
    department = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user.username} - {self.specialization}"

class Registrar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='registrar')
    office_location = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user.username} - Registrar"

class Issue(models.Model):
    STATUS_CHOICES = [
        ('open', 'Open'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
    ]
    
    category = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='open')
    submitted_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="submitted_issues")
    assigned_to = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name="assigned_issues")
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

    @staticmethod
    def create_notification(user, message):
        """Utility function to create notifications"""
        Notification.objects.create(user=user, message=message)
