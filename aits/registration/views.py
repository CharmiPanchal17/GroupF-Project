from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')

def register_student(request):
    return render(request, 'register_student.html')

def register_lecturer(request):
    return render(request, 'register_lecturer.html')

def login_user(request):
    return render(request, 'login_user.html')