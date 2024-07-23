from django.contrib import admin
from .models import *


@admin.register(UserModel)
class UserAdmin(admin.ModelAdmin):
    list_display = ['fullname', 'email', 'is_active']
