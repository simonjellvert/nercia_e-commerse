from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.core.serializers.json import DjangoJSONEncoder
from django.contrib import messages
from django.db.models import Q

from .models import Product, ProductContent, Category
from .forms import ProductForm, ProductContentForm, ProductContentFormSet

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

def add_product(request):
    """
    Add a new product
    """
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'You successfully added the new product!')
            return redirect('add_product_content', product_id=product.id)
        else:
            messages.error(request, 'Something went wrong, check if form is valid!')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

def add_product_content(request, product_id):
    """
    Add product content to product
    """
    product = Product.objects.get(id=product_id)
    if request.method == 'POST':
        form = ProductContentForm(request.POST)
        formset = ProductContentFormSet(request.POST, prefix='product_content')
        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            messages.success(request, f'Product content added to {product.name}')
            return redirect('products')
        else:
            messages.error(request, 'Something went wrong, check if form is valid!')
    else:
        form = ProductContentForm
        formset = ProductContentFormSet(prefix='product_content')

    template = 'products/add_product_content.html'
    context = {
        'form': form,
        'formset': formset,
    }

    return render(request, template, context)