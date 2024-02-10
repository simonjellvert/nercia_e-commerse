import uuid
from decimal import Decimal

from django.db import models
from django.db.models import Sum
from django.conf import settings
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError

from products.models import Product
from profiles.models import UserProfile
from bag.contexts import bag_contents


class Order(models.Model):
    """ Model for the order that sets up database with order information """
    INVOICE = 'invoice'
    CARD = 'card'

    PAYMENT_OPTIONS = [
        (INVOICE, 'Invoice'),
        (CARD, 'Card'),
    ]

    order_number = models.CharField(max_length=10, unique=True)
    user_profile = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        related_name='orders'
    )
    created = models.DateTimeField(auto_now_add=True)
    order_total = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        null=False,
        blank=False
    )
    grand_total = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        null=False,
        blank=False
    )
    tax = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        null=False,
        blank=False
    )
    payment_option = models.CharField(
        max_length=20,
        choices=PAYMENT_OPTIONS,
        default=INVOICE
    )
    invoice_ref = models.CharField(max_length=254, null=True, blank=True)

    def _generate_order_number(self):
        """ Generates a random and unique order number using UUID """
        return str(uuid.uuid4().int)[:10]

    def update_total(self):
        """ Update order_total and grand_total """
        lineitem_total_sum = self.lineitems.aggregate(
            Sum('lineitem_total'))['lineitem_total__sum'] or Decimal('0.00')
        self.order_total = lineitem_total_sum

        # Calculate tax based on order_total
        self.tax = self.order_total * Decimal('0.25')

        # Calculate grand_total including tax
        self.grand_total = self.order_total + self.tax

        self.save()

    def save(self, *args, **kwargs):
        """ Override original save method to set the order number """
        if not self.order_number:
            self.order_number = self._generate_order_number()

        super().save(*args, **kwargs)

    def __str__(self):
        return f"Order {self.order_number} - {self.user_profile.company_name}"


class OrderLineItem(models.Model):
    """ Sets the order line for the checkout """
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
    quantity = models.PositiveIntegerField(
        default=1,
        validators=[MinValueValidator(1)]
    )
    lineitem_total = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        null=False,
        blank=False,
        editable=False
    )
