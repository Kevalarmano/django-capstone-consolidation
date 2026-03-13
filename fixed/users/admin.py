"""Admin configuration for the users app."""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    """Admin panel configuration for CustomUser."""
    list_display = ['username', 'email', 'is_staff', 'date_joined']
    fieldsets = UserAdmin.fieldsets + (
        ('Profile', {'fields': ('bio',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Profile', {'fields': ('bio',)}),
    )
