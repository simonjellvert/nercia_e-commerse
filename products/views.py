from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.core.serializers.json import DjangoJSONEncoder
from .models import Product, ProductContent, Category
from django.contrib import messages
from django.db.models import Q
import json


def all_products(request):
    """
    A view to return products page
    """

    products = Product.objects.all()
    product_contents = ProductContent.objects.all()
    categories = Category.objects.all()
    query = None

    if 'category' in request.GET:
        category_name = request.GET['category']
        if category_name:
            products = products.filter(category__name=category_name)
            product_contents = product_contents.filter(product__category__name=category_name)

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
            else:
                queries = Q(name__icontains=query) | Q(description__icontains=query)
                products = products.filter(queries)
            
            if not products.exists():
                # Redirect to the main products page if there are no search results
                return redirect(reverse('products'))

            product_queries = Q(name__icontains=query) | Q(description__icontains=query)
            content_queries = Q(title__icontains=query) | Q(topics__icontains=query)

            products = products.filter(product_queries)
            product_contents = product_contents.filter(content_queries)

    context = {
        'products': products,
        'product_contents': product_contents,
        'categories': categories,
        'search_terms': query,
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

