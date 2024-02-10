from django.db import models


class Contact(models.Model):
    """ Model for contact persons """
    name = models.CharField(max_length=100, null=False, blank=True)
    email = models.EmailField(null=False, blank=False)
    phone_number = models.CharField(max_length=20, blank=False, null=False)
    image = models.ImageField(null=False, blank=False)

    def __str__(self):
        return self.name
