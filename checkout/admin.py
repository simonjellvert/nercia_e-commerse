from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemInline(admin.TabularInline):
    """ Sets up admin panel for products """
    model = OrderLineItem
    readonly_fields = ('product', 'quantity', 'lineitem_total')


class OrderAdmin(admin.ModelAdmin):
    """ Sets up admin panel for user information """
    inlines = (OrderLineItemInline,)

    readonly_fields = (
        'order_number',
        'created',
        'order_total',
        'grand_total',
        'tax',
    )

    fields = (
        'order_number',
        'created',
        'user_profile',
        'payment_option',
        'invoice_ref',
        'order_total',
        'grand_total',
    )

    list_display = (
        'order_number',
        'payment_option',
        'order_total',
        'grand_total',
    )

    ordering = ('-created',)


admin.site.register(Order, OrderAdmin)
