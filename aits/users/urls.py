from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('', views.home, name='home' ),
    path('register/lecturer/',views.register_lecturer, name='register_lecturer' ),
    path('register/student/',views.register_student, name='register_student' ),
    path('login/',views.login_user, name='login_user' ),
]
