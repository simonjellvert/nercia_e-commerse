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
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'name': 'Company Name',
            'org_num': 'Org. Number',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'postcode': 'Postal Code',
            'city': 'Town or City',
            'country': 'Country',
            'invoice_email': 'Invoice Email',
        }

        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False