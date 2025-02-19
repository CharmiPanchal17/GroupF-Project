from django.shortcuts import render, redirect
from .forms import StudentRegistrationForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from .models import Student

# Create your views here.
def home(request):
    return render(request, 'home.html')


def register_student(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            student = form.save()
            user = authenticate(username=student.username, password=request.POST["password1"])
            if user is not None:
                login(request, user)
            return redirect("issues:student_dashboard")
    else:
        form =StudentRegistrationForm()
    return render(request, 'register_student.html' , {"form":form})


def register_lecturer(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            return redirect("issues:lecturer_dashboard")
    else:
        form =UserCreationForm()
    return render(request, 'register_lecturer.html' , {"form":form})


def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('issues:student_dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {"form" : form })

def logout_user(request):
    logout(request)
    return redirect('users:home')


    
