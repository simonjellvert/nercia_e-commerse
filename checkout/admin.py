from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('product', 'quantity', 'lineitem_total')

class OrderAdmin(admin.ModelAdmin):
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