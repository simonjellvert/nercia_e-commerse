from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

class UserProfile(models.Model):
    """
    User profile model
    """
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        unique=True
    )
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    company_name = models.CharField(max_length=100, null=False, blank=False)
    org_num = models.CharField(max_length=20, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    postcode = models.CharField(max_length=20, null=False, blank=False)
    city = models.CharField(max_length=40, null=False, blank=False)
    country = CountryField(blank_label='Country', null=False, blank=False)
    invoice_email = models.EmailField(max_length=254, null=True, blank=True)
    invoice_ref = models.charfield(max_length=254, null=True, false=True)

    def __str__(self):
        return self.user.email


@receiver(post_save, sender=CustomUser)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        UserProfile.objects.create(user=instance)
        instance.userprofile.save()

