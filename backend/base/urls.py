from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import (
    register_user, login_user, logout_user, get_profile, submit_issue,
    assign_issue, resolve_issue, delete_issue
)

urlpatterns = [
    # Authentication
    path('register/', register_user, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  

    # Profile
    path('profile/', get_profile, name='get_profile'),

    # Issues
    path('issues/submit/', submit_issue, name='submit_issue'),
    path('issues/<int:issue_id>/assign/', assign_issue, name='assign_issue'),
    path('issues/<int:issue_id>/resolve/', resolve_issue, name='resolve_issue'),
    path('issues/<int:issue_id>/delete/', delete_issue, name='delete_issue'),
]
