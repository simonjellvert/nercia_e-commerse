from django.shortcuts import render
from .models import Product, ProductContent, Category


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
