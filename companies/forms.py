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