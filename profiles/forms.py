from allauth.account.forms import SignupForm
from django import forms
from django_countries.fields import CountryField

from .models import UserProfile


class CustomSignupForm(SignupForm):

    def __init__(self, *args, **kwargs):
        super(CustomSignupForm, self).__init__(*args, **kwargs)
        del self.fields['username']


class UserProfileForm(forms.ModelForm):
    newsletter_subscription = forms.BooleanField(
        label='Subscribe to Newsletter',
        required=False,
        initial=True,
        widget=forms.CheckboxInput(attrs={'class': 'stripe-style-input'}),
    )
    
    class Meta:
        model = UserProfile
        fields = [
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'company_name',
            'org_num',
            'street_address1',
            'street_address2',
            'postcode',
            'city',
            'country',
            'invoice_email',
            'newsletter_subscription',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email',
            'phone_number': 'Phone Number',
            'company_name': 'Company Name',
            'org_num': 'Org. Number',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'postcode': 'Postal Code',
            'city': 'City',
            'country': 'Country',
            'invoice_email': 'Invoice Email',
            'newsletter_subscription': 'Subscribe to Newsletter',
        }

        for field in self.fields:
            if field == 'newsletter_subscription':
                self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            elif self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
                self.fields[field].widget.attrs['placeholder'] = placeholder
                self.fields[field].widget.attrs['class'] = 'stripe-style-input'
                self.fields[field].label = False
            else:
                self.fields[field].widget.attrs['placeholder'] = placeholders[field]
                self.fields[field].widget.attrs['class'] = 'stripe-style-input'
                self.fields[field].label = False
    

# Form for delete profile with password authentication setup for future development
class DeleteAccountForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))