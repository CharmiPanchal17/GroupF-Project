from django.urls import path
from .views import RegisterStudentView, LoginView, StudentDashboardView, LecturerDashboardView, RegistrarDashboardView, RegisterLecturerView, RegisterRegistrarView
from rest_framework_simplejwt.views import TokenRefreshView

app_name = 'base'

urlpatterns = [
    #register users
    path('register/student/', RegisterStudentView.as_view(), name='register-student'),
    path('register/lecturer/', RegisterLecturerView.as_view(), name='register-lecturer'),
    path('register/registrar/', RegisterRegistrarView.as_view(), name='register-registrar'),

    #login users
    path('login/', LoginView.as_view(), name='login'),

    #token refresh
    path('login/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    #dashboards
    path('student/dashboard/', StudentDashboardView.as_view(), name='student-dashboard'),
    path('lecturer/dashboard/', LecturerDashboardView.as_view(), name='lecturer-dashboard'),
    path('registrar/dashboard/', RegistrarDashboardView.as_view(), name='registrar-dashboard'),
]