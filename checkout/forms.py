from django import forms

from .models import Order, ParticipantInfo
from profiles.forms import UserProfileForm
from companies.forms import CompanyForm


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
        
        user_profile_instance = kwargs.get('instance', None)
        company_instance = user_profile_instance.company if user_profile_instance else None

        self.user_profile_form = UserProfileForm(*args, instance=user_profile_instance)
        self.company_form = CompanyForm(*args, instance=company_instance)

        self.fields.update(self.user_profile_form.fields)
        self.fields.update(self.company_form.fields)

        placeholders = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'phone_number': 'Phone Number',
            'name': 'Company Name',
            'org_num': 'Org. Number',
            'country': 'Country',
            'postcode': 'Postal Code',
            'city': 'Town or City',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'invoice_email': 'Invoice Email',
            'invoice_ref': 'Invoice Referens',
        }

        for field_name, field in self.fields.items():
            field_key = field_name.lower()
            if field_name in placeholders:
                if field.required:
                    placeholder = f'{placeholders[field_key]} *'
                else:
                    placeholder = placeholders[field_key]
                field.widget.attrs['placeholder'] = placeholder
                field.widget.attrs['class'] = 'stripe-style-input'
                field.label = False

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


class ParticipantInfoForm(forms.ModelForm):
    class Meta:
        model = ParticipantInfo
        fields = ['participant_name', 'participant_email']
    
    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'participant_name': 'Participants Name',
            'participant_email': 'Participants Email'
        }

        self.fields['participant_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
