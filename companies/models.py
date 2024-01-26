from django.db import models
from django_countries.fields import CountryField

from django.conf import settings


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

    userprofile = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='user_profile',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name

