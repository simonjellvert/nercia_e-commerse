from django.contrib import admin
from .models import Category, Product, ProductContent


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'duration',
        'online_onsite',
        'price',
    )

    ordering = ('name',)


class ProductContentAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'title',
        'day',
    )

    ordering = ('product',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductContent, ProductContentAdmin)
