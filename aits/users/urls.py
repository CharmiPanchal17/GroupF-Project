from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegisterStudentView,LecturerViewSet, LoginView, StudentDashboardView, LecturerDashboardView, RegistrarDashboardView, RegisterLecturerView, RegisterRegistrarView
from rest_framework_simplejwt.views import TokenRefreshView

router = DefaultRouter()
router.register('lecturers', LecturerViewSet, basename='lecturers')

app_name = 'users'

urlpatterns = [
    path('', include(router.urls)),
    path('register/student/', RegisterStudentView.as_view(), name='register-student'),
    path('register/lecturer/', RegisterLecturerView.as_view(), name='register-lecturer'),
    path('register/registrar/', RegisterRegistrarView.as_view(), name='register-registrar'),
    path('login/', LoginView.as_view(), name='login'),
    path('login/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('student/dashboard/', StudentDashboardView.as_view(), name='student-dashboard'),
    path('lecturer/dashboard/', LecturerDashboardView.as_view(), name='lecturer-dashboard'),
    path('registrar/dashboard/', RegistrarDashboardView.as_view(), name='registrar-dashboard'),
]