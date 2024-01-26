from django import forms

from .models import Company


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
            'invoice_email': 'Invoice Email Address'
        }
