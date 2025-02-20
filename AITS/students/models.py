from django.db import models

# Create your models here.
class Studententry(models.Model):
    from django.db import models

class Student(models.Model):
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
        ('Li', ' Library andInformation Technology'),
        ('se', 'Software Engineering'),
    ]
    
    
    name=models.CharField(max_length=20)
    Student_ID=models.CharField(max_length=15, unique=True)
    Issue= models.TextField()
    Registered_at= models.DateTimeField(auto_now_add=True)
    email = models.EmailField(unique=True)
    year = models.CharField(max_length=1, choices=YEAR_CHOICES, default='1')
    course = models.CharField(max_length=2, choices=COURSE_CHOICES, default='cs')


    def __str__(self):
        return f"{self.name} - {self.get_year_display()} - {self.get_course_display()}"


