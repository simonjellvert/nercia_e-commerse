from django import forms
from .models import Newsletter


class NewsletterForm(forms.ModelForm):
    """
    Form for sending out lewsletters to newsletter subscribers
    """
    class Meta:
        model = Newsletter
        fields = [
            'title',
            'content',
            'newsletter_category',
        ]