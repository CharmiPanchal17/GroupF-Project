from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import IssueViewSet

router = DefaultRouter()
router.register(r'issues', IssueViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]

from django.urls import path
from .views import issue_list, issue_detail, assign_issue, user_notifications

urlpatterns = [
    path('issues/', issue_list, name='issue-list'),
    path('issues/<int:pk>/', issue_detail, name='issue-detail'),
    path('assign/', assign_issue, name='assign-issue'),
    path('notifications/', user_notifications, name='user-notifications'),
]