from django import forms
from django.forms.models import inlineformset_factory

from .models import Order, Participant
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
            'user_profile',
            'order_total',
            'grand_total',
            'tax',
            'payment_option',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        placeholders = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email',
            'phone_number': 'Phone Number',
            'company_name': 'Company Name',
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

        self.participant_info_formset = ParticipantInfoFormSet(
            prefix='participants',
        )

    def is_valid(self):
        return super().is_valid() and self.user_profile_form.is_valid()

    def save(self, commit=True):
        order = super().save(commit=False)

        # Get or create user profile based on the form data
        user_profile_instance, _ = UserProfile.objects.get_or_create(
            user=self.cleaned_data['user_profile']
        )

        # Update order with the user profile
        order.user_profile = user_profile_instance
        order.save()

        # Calculate and update order totals
        order.update_total()

        if self.errors:
            print("Form validation errors:", self.errors)

        if commit:
            order.save()

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
