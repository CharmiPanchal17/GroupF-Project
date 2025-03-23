from django.urls import path
from .views import (
    register_user, login_user, submit_issue, assign_issue, 
    student_dashboard, lecturer_dashboard, registrar_dashboard,
    get_notifications
)

urlpatterns = [
    path('register/', register_user, name='register'),
    path('login/', login_user, name='login'),
    
    # Issue Management
    path('submit-issue/', submit_issue, name='submit-issue'),
    path('assign-issue/<int:issue_id>/', assign_issue, name='assign-issue'),

    # Dashboards
    path('dashboard/student/', student_dashboard, name='student-dashboard'),
    path('dashboard/lecturer/', lecturer_dashboard, name='lecturer-dashboard'),
    path('dashboard/registrar/', registrar_dashboard, name='registrar-dashboard'),

    # Notifications
    path('notifications/', get_notifications, name='get-notifications'),
]
