from django.urls import path
from . import views

app_name = 'issues'

urlpatterns = [
    path('issues/student_dashboard/', views.student_dashboard, name='student_dashboard'),
    path('issues/lecturer_dashboard/', views.lecturer_dashboard, name='lecturer_dashboard'),
    path('issues/submit_complaint/', views.submit_complaint, name='submit_complaint'),
]

