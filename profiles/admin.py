from django.contrib import admin
from .models import UserProfile
from companies.models import Company


class ProfilesAdmin(admin.ModelAdmin):
    list_display = (
        'user',
    )


class CompaniesAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


admin.site.register(UserProfile, ProfilesAdmin)
admin.site.register(Company, CompaniesAdmin)
