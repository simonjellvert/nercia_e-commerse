from django.db import models
from django.db.models import Sum, F
from products.models import Product

class PromoCode(models.Model):
    code = models.CharField(max_length=20, unique=True)
    discount_type = models.CharField(
        max_length=20,
        choices=[
            ('percentage', 'Percentage'),
            ('product', 'Product'),
            ('buy_x_get_y', 'Buy X Get Y'),
        ],
        default='percentage'
    )
    discount_amount = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    product_discounted = models.ForeignKey(
        Product,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='discounted_product',
        help_text='Relevant for product-specific discounts or "Buy X Get Y" discounts'
    )
    buy_x_quantity = models.IntegerField(
        null=True,
        blank=True,
        help_text='Relevant for "Buy X Get Y" discounts. The quantity to buy (X).'
    )
    get_y_quantity = models.IntegerField(
        null=True,
        blank=True,
        help_text='Relevant for "Buy X Get Y" discounts. The quantity to get for free (Y).'
    )
    start_date = models.DateTimeField(
        null=True,
        blank=True,
        help_text='The start date of the promo code validity'
    )
    end_date = models.DateTimeField(
        null=True,
        blank=True,
        help_text='The end date of the promo code validity'
    )

    def __str__(self):
        return self.code

    def is_active(self):
        """
        Check if the promo code is currently active based on the start and end dates.
        """
        now = datetime.now()
        return (
            self.start_date <= now <= self.end_date
        ) if self.start_date and self.end_date else True


    def apply_promo_code(order, promo_code):
        """
        Apply discount based on the given promo code to the order.
        """
        if not promo_code:
            return

        # Calculate the current order total without the promo code
        order_total = (
            order.lineitems
            .aggregate(Sum('lineitem_total'))
            .get('lineitem_total__sum', 0)
        )

        if order_total == 0:
            return  # Prevent division by zero

        if promo_code.discount_type == 'percentage':
            # Calculate the discount based on the percentage
            discount_amount = order_total * (promo_code.discount_amount / 100)
        elif promo_code.discount_type == 'product':
            # Calculate the product-specific discount
            product_discounted_total = (
                order.lineitems
                .filter(product=promo_code.product_discounted)
                .aggregate(Sum('lineitem_total'))
                .get('lineitem_total__sum', 0)
            )
            discount_amount = product_discounted_total * promo_code.discount_amount
        elif promo_code.discount_type == 'buy_x_get_y':
            # Calculate the "Buy X Get Y" discount
            product_discounted_quantity = (
                order.lineitems
                .filter(product=promo_code.product_discounted)
                .aggregate(Sum('quantity'))['quantity__sum'] or 0)
            discount_amount = (
                product_discounted_quantity // promo_code.buy_x_quantity
            ) * promo_code.get_y_quantity * promo_code.discount_amount

        # Update the order total with the discount
        order_total -= discount_amount

        # Apply the discount to each line item
        order.lineitems.update(
            lineitem_total=F('lineitem_total') -
                        (F('lineitem_total') / order_total *
                            discount_amount)
        )

        # Update the grand total and save the order
        order.grand_total = order_total
        order.promo_code = promo_code
        order.save()
