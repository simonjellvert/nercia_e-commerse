from django import forms
from django.forms.models import inlineformset_factory

from .models import Order, Participant
from profiles.forms import UserProfileForm
from companies.forms import CompanyForm
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
    invoice_ref = forms.CharField(max_length=254, required=False)

    class Meta:
        model = Order
        fields = (
            'user_profile', 'company_name', 'order_total',
            'grand_total', 'promo_code', 'tax', 'payment_option',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        user_profile = forms.ModelChoiceField(queryset=UserProfile.objects.all(), widget=forms.HiddenInput())
        
        user_profile_instance = kwargs.get('instance', None)
        company_instance = user_profile_instance.company if user_profile_instance and user_profile_instance.company else None

        self.user_profile_form = UserProfileForm(*args, instance=user_profile_instance)
        self.company_form = CompanyForm(*args, instance=company_instance)

        # Update fields and widgets
        self.fields.update(self.user_profile_form.fields)
        self.fields.update(self.company_form.fields)

        # Set initial values for user_profile_form and company_form
        if user_profile_instance:
            self.user_profile_form.initial = user_profile_instance.__dict__
        if company_instance:
            self.company_form.initial = company_instance.__dict__

        # Update widgets with initial values
        for field in self.fields:
            if field in self.user_profile_form.fields:
                self.fields[field].widget.attrs['value'] = self.user_profile_form[field].value()
            elif field in self.company_form.fields:
                self.fields[field].widget.attrs['value'] = self.company_form[field].value()

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
    
        ParticipantInfoFormSet = inlineformset_factory(
            Product,
            Participant,
            form=ParticipantInfoForm,
            extra=1,
            can_delete=False
        )

        # Correct indentation for ParticipantInfoFormSet
        self.participant_info_formset = ParticipantInfoFormSet(
            prefix='participants',
        )

    def is_valid(self):
        return super().is_valid() and self.user_profile_form.is_valid() and self.company_form.is_valid()

    def save(self, commit=True):
        order = super().save(commit)

        user_profile = self.user_profile_form.save(commit=False)
        if not user_profile.user:
            raise ValueError("User should be associated with the UserProfile.")

        order.user = user_profile.user
        user_profile.save()

        company = self.company_form.save(commit=False)
        company.user_profile = user_profile
        company.save()

        if order.errors:
            print("Order validation errors:", order.errors)  # Add this line for debugging

        print("Order created successfully")

        return order


class ParticipantInfoForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['participant_name', 'participant_email']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'participant_name': 'Participants Name',
            'participant_email': 'Participants Email'
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
