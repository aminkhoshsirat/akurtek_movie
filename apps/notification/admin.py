from django.contrib import admin
from .models import *


@admin.register(NotificationModel)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ['title', 'image']