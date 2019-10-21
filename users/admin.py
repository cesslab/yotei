from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Manager


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ['email', 'username', 'full_name', 'role']
    fieldsets = (
        (None, {'fields': ('full_name', 'role',)}),
    ) + UserAdmin.fieldsets


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Manager)
