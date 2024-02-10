from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """ Form for adding a contact person """

    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone_number', 'image']
