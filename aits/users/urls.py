from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegisterLecturerView, RegisterStudentView, RegisterRegistrarView, LecturerViewSet

router = DefaultRouter()
router.register('lecturers', LecturerViewSet, basename='lecturers')

urlpatterns = [
    path('', include(router.urls)),
    path('register/student/', RegisterStudentView.as_view(), name='register-student'),
    path('register/lecturer/', RegisterLecturerView.as_view(), name='register-lecturer'),
    path('register/registrar/', RegisterRegistrarView.as_view(), name='register-registrar'),
]
