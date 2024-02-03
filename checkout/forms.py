from django import forms
from django.forms.models import inlineformset_factory

from .models import Order
from profiles.forms import UserProfileForm
from products.models import Product
from profiles.models import UserProfile


class CheckoutForm(forms.ModelForm):
    """
    Choices to pay with card or invoice.
    if user chose invoice, they need to add invoice_ref to the order info
    """
    payment_option = forms.ChoiceField(choices=[], required=True)
    invoice_ref = forms.CharField(max_length=255, required=False)

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

        self.fields['payment_option'].choices = self.get_payment_options()

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
    
    def get_payment_options(self):
        """
        Logic to fetch payment option dynamically
        """
        return [
            ('invoice', 'Invoice'),
            ('card', 'Card'),
        ]

    def save(self, commit=True):
        order = super().save(commit=False)

        if not order.order_number:
            order.order_number = order._generate_order_number()

        # Update order with the user profile
        order.user_profile = user.user.profile

        if commit:
            order.save()

        return order
