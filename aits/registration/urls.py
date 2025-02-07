from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register_student/', views.register_student, name='register_student'),
    path('register_lecturer/', views.register_lecturer, name='register_lecturer'),
    path('login_user/', views.login_user, name='login_user'),
]
