from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
#@login_required(login_url="/login/")
def student_dashboard(request):
    return render(request, 'student_dashboard.html')

def lecturer_dashboard(request):
    return render(request, 'lecturer_dashboard.html')

def submit_complaint(request):
    return render(request, 'submit_complaint.html')

