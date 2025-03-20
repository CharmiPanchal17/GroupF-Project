from django.contrib import admin
from .models import User, Student, Lecturer, Registrar, Issue, Notification

admin.site.register(User)
admin.site.register(Student)
admin.site.register(Lecturer)
admin.site.register(Registrar)
admin.site.register(Issue)
admin.site.register(Notification)
