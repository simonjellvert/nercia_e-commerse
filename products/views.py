from django.shortcuts import render
from .models import Product, ProductContent


def all_products(request):
    """
    A view to return products page
    """

    products = Product.objects.all()
    product_contents = ProductContent.objects.all()

    context = {
        'products': products,
        'product_contents': product_contents,
    }

    return render(request, 'products/products.html', context)
