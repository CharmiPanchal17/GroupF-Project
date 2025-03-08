from django.urls import path
from .views import (
    create_user, list_users, create_student, list_students, create_lecturer, list_lecturers,
    create_registrar, list_registrars, create_issue, list_issues, assign_issue, resolve_issue, list_notifications
)

urlpatterns = [
    path('users/', list_users, name='list_users'),
    path('users/create/', create_user, name='create_user'),

    path('students/', list_students, name='list_students'),
    path('students/create/', create_student, name='create_student'),

    path('lecturers/', list_lecturers, name='list_lecturers'),
    path('lecturers/create/', create_lecturer, name='create_lecturer'),

    path('registrars/', list_registrars, name='list_registrars'),
    path('registrars/create/', create_registrar, name='create_registrar'),

    path('issues/', list_issues, name='list_issues'),
    path('issues/create/', create_issue, name='create_issue'),
    path('issues/assign/<int:issue_id>/<int:lecturer_id>/', assign_issue, name='assign_issue'),
    path('issues/resolve/<int:issue_id>/', resolve_issue, name='resolve_issue'),

    path('notifications/', list_notifications, name='list_notifications'),
]
