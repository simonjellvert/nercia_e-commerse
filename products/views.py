from django.shortcuts import render, get_object_or_404
from .models import Product, ProductContent, Category
from django.core.serializers.json import DjangoJSONEncoder
from django.utils.html import json_script
import json


def all_products(request):
    """
    A view to return products page
    """

    products = Product.objects.all()
    product_contents = ProductContent.objects.all()
    categories = Category.objects.all()

    context = {
        'products': products,
        'product_contents': product_contents,
        'categories': categories,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """
    A view to return details about a product
    """

    product = get_object_or_404(Product, pk=product_id)
    product_contents = ProductContent.objects.filter(product=product)

    for product_content in product_contents:
        topics = product_content.topics
        if isinstance(topics, str):
            # Split the string and strip quotes and brackets
            product_content.topics = [topic.strip(" '[]") for topic in topics.split(',')]

    context = {
        'product': product,
        'product_contents': product_contents,
    }

    return render(request, 'products/product_detail.html', context)

