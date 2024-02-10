from django.contrib import admin
from .models import Newsletter


class NewsletterAdmin(admin.ModelAdmin):
    """ Sets up admin panel for newsletters """
    list_display = ('title', 'newsletter_category', 'created_at')
    list_filter = ('newsletter_category', 'created_at')
    search_fields = ('title', 'content')
    date_hierarchy = 'created_at'


admin.site.register(Newsletter, NewsletterAdmin)
