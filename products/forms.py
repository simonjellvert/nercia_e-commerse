from django import forms
from django.forms import inlineformset_factory

from .models import Product, Category, ProductContent


class ProductForm(forms.ModelForm):
    categories = Category.objects.all()
    friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

    category = forms.MultipleChoiceField(
        choices=friendly_names,
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Product
        fields = [
            'name', 'description_short',
            'description', 'category',
            'price', 'duration', 'perks',
            'image', 'alt_atr', 'online_onsite',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'

class ProductContentForm(forms.ModelForm):
    class Meta:
        model = ProductContent
        fields = ['day', 'title', 'purpose', 'topics']

ProductContentFormSet = inlineformset_factory(
    Product,
    ProductContent,
    form=ProductContentForm,
    extra=1,
    can_delete=True,
)