from django.contrib import admin
from .models import Company
from profiles.models import UserProfile

class CompanyInline(admin.StackedInline):
    model = Company
    extra = 1

class UserProfileAdmin(admin.ModelAdmin):
    inlines = [CompanyInline]

admin.site.register(UserProfile, UserProfileAdmin)