from django.db import models


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):

    COMBINED = 'combined'
    ONSITE = 'onsite'
    ONLINE = 'online'
    OPTIONAL = 'optional'

    ONLINE_ONSITE_CHOICES = [
        (COMBINED, 'Combined'),
        (ONSITE, 'Onsite'),
        (ONLINE, 'Online'),
        (OPTIONAL, 'Optional'),
    ]

    name = models.CharField(max_length=254)
    description_short = models.TextField()
    description = models.TextField(default='Description of the training')
    category = models.ManyToManyField(Category, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    duration = models.CharField(max_length=254, null=True, blank=True)
    perks = models.CharField(max_length=254, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    alt_atr = models.CharField(max_length=254, null=True, blank=True)
    online_onsite = models.CharField(
        max_length=20,
        choices=ONLINE_ONSITE_CHOICES,
        default=ONSITE,
    )

    def __str__(self):
        return self.name


class ProductContent(models.Model):
    product = models.ForeignKey(
        'Product', null=True, blank=True, on_delete=models.SET_NULL
    )
    day = models.CharField(max_length=254, null=True, blank=True)
    title = models.CharField(max_length=254, null=True, blank=True)
    purpose = models.TextField(null=True, blank=True)
    topics = models.TextField(null=True, blank=True)

    def __str__(self):
        product_name = self.product.name if self.product else 'No Product'
        return f"{product_name} - {self.title}"
