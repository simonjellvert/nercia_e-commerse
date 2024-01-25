from django.db import models

from django_countries.fields import CountryField


class Company(models.Model):
    """
    Model for the user to add billing information to a company
    """
    name = models.CharField(max_length=100, unique=True)
    org_num = models.CharField(max_length=20, unique=True)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    postcode = models.CharField(max_length=20, null=False, blank=False)
    city = models.CharField(max_length=40, null=False, blank=False)
    country = CountryField(blank_label='Country', null=False, blank=False)
    invoice_email = models.EmailField(max_length=254, null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.org_num})"


class Address(models.Model):
    """
    A model to be able to store several addresses to a specific comapny
    """
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    postcode = models.CharField(max_length=20, null=False, blank=False)
    city = models.CharField(max_length=40, null=False, blank=False)
    country = models.CharField(max_length=40, null=False, blank=False)
