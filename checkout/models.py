import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings

from products.models import Product
from profiles.models import UserProfile, CompanyName, Address


class Order(models.Model):
    INVOICE = 'invoice'
    CARD = 'card'

    PAYMENT_OPTIONS = [
        (INVOICE, 'Invoice'),
        (CARD, 'Card'),
    ]

    order_number = models.CharField(max_length=32, null=False, editable=False)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    company_name = models.ForeignKey(
        CompanyName,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    billing_address = models.ForeignKey(
        Address,
        related_name='billing_address',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    order_total = models.DecimalField(max_digits=8, decimal_places=2, null=False, blank=False)
    grand_total = models.DecimalField(max_digits=8, decimal_places=2, null=False, blank=False)
    promo_code = ForeignKey(
        PromoCode,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    tax = models.DecimalField(max_digits=8, decimal_places=2, null=False, blank=False)
    payment_option = models.CharField(max_length=20, choices=PAYMENT_OPTIONS, default=INVOICE)

    # Additional fields for invoice payment option
    invoice_email = models.EmailField(max_length=254, null=True, blank=True)
    invoice_ref = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return f"Order {self.order_number}"
    
    def clean(self):
        """
        If payment_option is 'invoice', ensure that invoice_email and 
        invoice_ref are provided
        """
        if self.payment_option == self.INVOICE and (
            not self.invoice_email or not self.invoice_ref):
            raise models.ValidationError(
                "Both invoice email and invoice reference are "
                "required for invoice payment option.")

    def _generate_order_number(self):
        """
        Generates a random and unique order number using UUID
        """
        return uuid.uuid4().hex.upper()
    
    def save(self, *args, **kwargs):
        """
        Override original save method to set the order number
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)


class OrderLineItem(models.Model):
    order = models.ForeignKey(
        Order,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name='lineitems'
    )
    product = models.ForeignKey(
        Product,
        null=False,
        blank=False,
        on_delete=models.CASCADE
    )
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        null=False,
        blank=False,
        editable=False
    )
