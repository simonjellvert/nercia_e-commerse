from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    """ Admin setup for contacts in the admin panel """
    list_display = (
        'name',
        'phone',
        'email',
        'image',
    )


admin.site.register(Contact)
