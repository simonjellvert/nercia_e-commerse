from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from companies.models import Company


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
    companies = models.ManyToManyField(Company, through='UserCompany')

    def __str__(self):
        return self.user.email

class UserCompany(models.Model):
    """
    A model for the user to be able to choose between different 
    commpanies that they represent
    """
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    is_primary = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user_profile.user.email} - {self.company.name}"


@receiver(post_save, sender=CustomUser)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        UserProfile.objects.create(user=instance)
    # Existing users: just save the profile
    instance.userprofile.save()
