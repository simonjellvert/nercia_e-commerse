from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, UserProfile


class UserProfileInline(admin.StackedInline):
    model = UserProfile


class CustomUserAdmin(UserAdmin):
    inlines = [UserProfileInline]


admin.site.register(CustomUser, CustomUserAdmin)