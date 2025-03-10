from django.shortcuts import render
from .models import Student
# Create your views here.
def home(request):
    return render(request,"base.html")

def student(request):
    items = Student.objects.all()
    return render(request, 'login.html', {'student':items})