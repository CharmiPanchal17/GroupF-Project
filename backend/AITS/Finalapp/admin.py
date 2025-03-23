from django.contrib import admin
from .models import CustomUser,StudentProfile ,LecturerProfile,RegistrarProfile ,Issue,Assignment,Notification

# Register your models here.

# Customizing admin views
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'role', 'is_active', 'is_staff')
    list_filter = ('role', 'is_active')
    search_fields = ('username', 'email')

class IssueAdmin(admin.ModelAdmin):
    list_display = ('title', 'student', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('title', 'student__username')

class AssignmentAdmin(admin.ModelAdmin):
    list_display = ('issue', 'lecturer', 'assigned_at')
    list_filter = ('assigned_at',)
    search_fields = ('lecturer__username', 'issue__title')

class NotificationAdmin(admin.ModelAdmin):
    list_display = ('recipient', 'message', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('recipient__username', 'message')




admin.site.register(CustomUser, UserAdmin)
admin.site.register(StudentProfile)
admin.site.register(LecturerProfile)
admin.site.register(RegistrarProfile)
admin.site.register(Issue, IssueAdmin)
admin.site.register(Assignment, AssignmentAdmin)
admin.site.register(Notification, NotificationAdmin)
