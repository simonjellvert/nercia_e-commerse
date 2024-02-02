from django import forms
from django.forms.models import inlineformset_factory

from .models import Order
from profiles.forms import UserProfileForm
from products.models import Product
from profiles.models import UserProfile


class CheckoutForm(forms.ModelForm):
    INVOICE = 'invoice'
    CARD = 'card'

    PAYMENT_OPTIONS = [
        (INVOICE, 'Invoice'),
        (CARD, 'Card'),
    ]

    payment_option = forms.ChoiceField(choices=PAYMENT_OPTIONS, required=True)

    class Meta:
        model = Order
        fields = (
            'order_total',
            'grand_total',
            'tax',
            'payment_option',
            'invoice_ref',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        placeholders = {
            'invoice_ref': 'Invoice Referens',
        }

        for field in self.fields:
            if field in placeholders:
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
                self.fields[field].widget.attrs['class'] = 'stripe-style-input'
                self.fields[field].label = False
            else:
                pass

    def save(self, commit=True):
        order = super().save(commit=False)

        # Ensure that order.user_profile is set
        if not order.user_profile:
            raise ValueError("Order has no user_profile.")

        # Get or create user profile based on the form data
        user_profile_instance, _ = UserProfile.objects.get_or_create(
            user=order.user_profile
        )

        # Update order with the user profile
        order.user_profile = user_profile_instance
        order.save()

        return order
