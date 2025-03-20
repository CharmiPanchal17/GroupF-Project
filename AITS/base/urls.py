from django.urls import path
from .views import (
    register_user, login_user, submit_issue, assign_issue, resolve_issue,
    list_issues, list_notifications
)

urlpatterns = [
    # User authentication
    path('register/', register_user, name='register_user'),
    path('login/', login_user, name='login_user'),

    # Issues
    path('issues/', list_issues, name='list_issues'),
    path('issues/submit/', submit_issue, name='submit_issue'),
    path('issues/assign/<int:issue_id>/', assign_issue, name='assign_issue'),
    path('issues/resolve/<int:issue_id>/', resolve_issue, name='resolve_issue'),

    # Notifications
    path('notifications/', list_notifications, name='list_notifications'),
]
