from django import forms

from .models import Order

from profiles.models import UserProfile


class CheckoutForm(forms.ModelForm):
    """
    Choices to pay with card or invoice.
    if user chose invoice, they need to add invoice_ref to the order info
    """
    invoice_ref = forms.CharField(max_length=255, required=False)

    class Meta:
        model = Order
        fields = (
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
        """ Logic to fetch payment option dynamically """
        return [
            ('invoice', 'Invoice'),
            ('card', 'Card'),
        ]

    def clean(self):
        """ 
        Ensures invoice_ref is submitted when checking out using invoice
        """
        cleaned_data = super().clean()
        payment_option = cleaned_data.get('payment_option')
        invoice_ref = cleaned_data.get('invoice_ref')

        if payment_option == 'invoice' and not invoice_ref:
            self.add_error(
                'invoice_ref', 'This field is required for invoice payments.'
            )

        return cleaned_data

    def save(self, commit=True):
        """ Overrides the save method """
        order = super().save(commit=False)

        if not order.order_number:
            order.order_number = order._generate_order_number()

        order.user_profile = user.user.profile
        order.invoice_ref = self.cleaned_data.get('invoice_ref')

        if commit:
            order.save()

        return order
