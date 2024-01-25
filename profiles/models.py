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
    companies = models.ForeignKey(
        Company,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.user.email


@receiver(post_save, sender=CustomUser)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        UserProfile.objects.create(user=instance)
    # Existing users: just save the profile
    instance.userprofile.save()
