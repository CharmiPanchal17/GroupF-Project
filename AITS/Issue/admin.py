from django.contrib import admin
from .models import Notification,CustomUser,Issue,Assignment


# Register your models here.
admin.site.register(Issue)
admin.site.register(CustomUser)
admin.site.register(Notification)

admin.site.register(Assignment)