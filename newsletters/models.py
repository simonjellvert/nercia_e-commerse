from django.db import models


class Newsletter(models.Model):
    """ Model for creating newsletters to subscribers """
    NEWSLETTER_CATEGORIES = [
        ('general', 'General'),
        ('promotions', 'Promotions'),
        ('product_updates', 'Product Updates'),
    ]

    title = models.CharField(max_length=254, blank=False, null=False)
    content = models.TextField(blank=False, null=False)
    newsletter_category = models.CharField(
        max_length=20,
        choices=NEWSLETTER_CATEGORIES,
        default='general'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
