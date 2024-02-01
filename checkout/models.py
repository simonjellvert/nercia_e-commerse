import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings
from django.core.validators import MinValueValidator

from products.models import Product
from profiles.models import UserProfile
from bag.models import PromoCode
from bag.contexts import bag_contents


class Order(models.Model):
    INVOICE = 'invoice'
    CARD = 'card'

    PAYMENT_OPTIONS = [
        (INVOICE, 'Invoice'),
        (CARD, 'Card'),
    ]

    order_number = models.CharField(max_length=32, null=False, editable=False)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='orders')
    created = models.DateTimeField(auto_now_add=True)
    order_total = models.DecimalField(max_digits=8, decimal_places=2, null=False, blank=False)
    grand_total = models.DecimalField(max_digits=8, decimal_places=2, null=False, blank=False)
    tax = models.DecimalField(max_digits=8, decimal_places=2, null=False, blank=False)
    payment_option = models.CharField(max_length=20, choices=PAYMENT_OPTIONS, default=INVOICE)
    
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
    
    def update_total(self):
        """
        Update order_total, grand_total based on line items and promo code
        """
        # Calculate line item total sum
        lineitem_total_sum = self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total__sum'] or Decimal('0.00')
        self.order_total = lineitem_total_sum

        # Apply promo code discount if available
        if self.promo_code:
            promo_discount = self.promo_code.calculate_discount(self.order_total)
            self.grand_total = self.order_total - promo_discount
        else:
            self.grand_total = self.order_total

        # Calculate tax as 25% of grand total
        self.tax = self.grand_total * Decimal('0.25')

        # Update order_total to include tax
        self.order_total = self.grand_total + self.tax

        self.save()

    def calculate_grand_total_with_promo_code(self):
        """
        Calculate grand_total with promo code discount
        """
        promo_discount = self.promo_code.calculate_discount(self.order_total)
        return self.order_total - promo_discount

    def save(self, *args, **kwargs):
        """
        Override original save method to set the order number
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        if not self.full_name:
            self.full_name = f"{self.user_profile.first_name} {self.user_profile.last_name}"

        super().save(*args, **kwargs)

    def __str__(self):
        return f"Order {self.order_number} - {self.full_name}"


class Participant(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    participant_name = models.CharField(max_length=255, null=False, blank=False)
    participant_email = models.EmailField(null=False, blank=False)
    quantity = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1)])

    # Remove this if not working
    participant_identifier = models.CharField(max_length=255, null=True, blank=True)   

    def __str__(self):
        return f"{self.participant_name} - {self.participant_email} ({self.quantity} x {self.product.name})"


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
