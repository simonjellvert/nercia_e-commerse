from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = (
        'order_number',
        'created',
        'order_total',
        'grand_total'
    )

    fields = (
        'order_number',
        'created',
        'user_profile',
        'company',
        'payment_option',
        'invoice_ref',
        'order_total',
        'promo_code',
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