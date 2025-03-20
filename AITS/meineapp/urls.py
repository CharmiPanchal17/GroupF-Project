from django.urls import path
from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import IssueViewSet, AssignmentViewSet, NotificationViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


router = DefaultRouter()
router.register(r'issues', IssueViewSet)
router.register(r'assignments', AssignmentViewSet)
router.register(r'notifications', NotificationViewSet)

 
urlpatterns = [
    path("",views.home ,name='home'),
    path("student/", views.student, name="Students"),
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]