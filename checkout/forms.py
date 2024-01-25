from django import forms

from .models import Order
from profiles.forms import UserProfileForm, CompanyForm

class CheckoutForm(forms.ModelForm):
    INVOICE = 'invoice'
    CARD = 'card'

    PAYMENT_OPTIONS = [
        (INVOICE, 'Invoice'),
        (CARD, 'Card'),
    ]

    payment_option = forms.ChoiceField(choices=PAYMENT_OPTIONS, required=False)
    invoice_ref = forms.CharField(max_length=254, required=False)

    class Meta:
        model = Order
        fields = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.user_profile_form = UserProfileForm(*args, **kwargs)
        self.company_form = CompanyForm(*args, **kwargs)

        self.fields.update(self.user_profile_form.fields)
        self.fields.update(self.company_form.fields)

    def is_valid(self):
        return super().is_valid() and self.user_profile_form.is_valid() and self.company_form.is_valid()

    def save(self, commit=True):
        order = super().save(commit)

        user_profile = self.user_profile_form.save(commit=False)
        user_profile.user = order.user_profile.user
        user_profile.save()

        company = self.company_form.save(commit=False)
        company.user_profile = user_profile
        company.save()

        return order
