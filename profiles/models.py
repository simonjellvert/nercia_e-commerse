from django.contrib.auth.models import User
from django.db import models
from companies.models import Company

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    companies = models.ManyToManyField(Company, through='UserCompany')
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return self.user.username

class UserCompany(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    is_primary = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user_profile.user.username} - {self.company.name}"
