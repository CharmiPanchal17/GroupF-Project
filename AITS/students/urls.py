from django.urls import path
from . import views
from  students.views import get_user ,create_user 

urlpatterns=[
    path ("",views.studentdata, name="Students"),
    path("users/",get_user , name="Get_users"),
    path("users/create/",create_user , name="Create_users"),
    path("users/<int:pk>",create_user , name="Create_users"),
    
]