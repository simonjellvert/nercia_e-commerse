from allauth.account.forms import SignupForm
from django import forms
from django_countries.fields import CountryField

from .models import UserProfile
from companies.models import Company
from checkout.models import Order

class CustomSignupForm(SignupForm):
    """
    Custom signup form to remove username
    """

    def __init__(self, *args, **kwargs):
        super(CustomSignupForm, self).__init__(*args, **kwargs)
        del self.fields['username']


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'first_name',
            'last_name',
            'phone_number'
        ]
        placeholders = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'phone_number': 'Phone Number'
        }

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = [
            'name',
            'org_num',
            'street_address1',
            'street_address2',
            'postcode',
            'city',
            'country',
            'invoice_email'
        ]
        placeholder = {
            'name': 'Company Name',
            'org_num': 'Organization number',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'postcode': 'Postal Code',
            'city': 'City',
            'country': 'Country',
            'invoice_email': 'Invoice Email Adress'
        }
