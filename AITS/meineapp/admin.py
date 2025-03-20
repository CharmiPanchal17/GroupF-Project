from django.contrib import admin
from .models import Student,Notification,CustomUser,Issue,Assignment

# Register your models here.
admin.site.register(Student)
admin.site.register(CustomUser)
admin.site.register(Notification)
admin.site.register(Issue)
admin.site.register(Assignment)
