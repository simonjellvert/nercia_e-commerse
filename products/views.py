from django.shortcuts import render, get_object_or_404
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


def product_detail(request, product_id):
    """
    A view to return details about a product
    """

    product = get_object_or_404(Product, pk=product_id)
    product_contents = ProductContent.objects.filter(product=product)

    context = {
        'product': product,
        'product_contents': product_contents,
    }

    return render(request, 'products/product_detail.html', context)

