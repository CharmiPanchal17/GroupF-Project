from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('', views.home, name='home' ),
    path('register/lecturer/',views.register_lecturer, name='register_lecturer' ),
    path('register/student/',views.register_student, name='register_student' ),
    path('login_student/',views.login_student, name='login_student' ),
    path('login_lecturer/',views.login_lecturer, name='login_lecturer' ),
    path('logout/',views.logout_user, name='logout_user' ),
]

