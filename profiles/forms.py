from allauth.account.forms import SignupForm
from django import forms
from django_countries.fields import CountryField

from .models import UserProfile


class CustomSignupForm(SignupForm):
    """
    Custom signup form to remove username
    """

    def __init__(self, *args, **kwargs):
        super(CustomSignupForm, self).__init__(*args, **kwargs)
        del self.fields['username']


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            'first_name',
            'last_name',
            'phone_number'
        ]
        placeholder = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'phone_number': 'Phone Number'
        }
