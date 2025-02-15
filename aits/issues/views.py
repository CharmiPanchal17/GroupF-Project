from django.shortcuts import render

# Create your views here.
def student_dashboard(request):
    return render(request, 'student_dashboard.html')

def lecturer_dashboard(request):
    return render(request, 'lecturer_dashboard.html')

def submit_complaint(request):
    return render(request, 'submit_complaint.html')

