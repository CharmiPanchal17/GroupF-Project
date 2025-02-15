from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.
def home(request):
    return render(request, 'home.html')


def register_lecturer(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("issues:lecturer_dashboard")
    else:
        form =UserCreationForm()
    return render(request, 'register_lecturer.html' , {"form":form})


def register_student(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("issues:student_dashboard")
    else:
        form =UserCreationForm()
    return render(request, 'register_student.html' , {"form":form})


def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
        #LOGIN
            return redirect('issues:student_dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {"form" : form })


    
