from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.core.serializers.json import DjangoJSONEncoder
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from .models import Product, ProductContent, Category
from .forms import ProductForm, ProductContentForm, ProductContentFormSet, CategoryForm

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

@staff_member_required
def product_management(request):
    """
    A view for administrators to either add new product or edit or delete excisting prodducts
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect('home')

    products = Product.objects.all()
    categories = Category.objects.all()

    if request.method == 'POST':
        if 'add_product' in request.POST:
            return redirect('add_product')

    template = 'products/product_management.html'
    context = {
        'products': products,
        'categories': categories,
    }

    return render(request, template, context)


@staff_member_required
def add_product(request):
    """
    Add a new product
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, f'You successfully added {product.name} to the store!')
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

@staff_member_required
def add_product_content(request, product_id):
    """
    Add product content to product, from ProgramContent model
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    product = Product.objects.get(id=product_id)

    if request.method == 'POST':
        formset = ProductContentFormSet(request.POST, instance=product, prefix='product_content')

        if formset.is_valid():
            formset.save()

            if 'add_day' in request.POST:
                print("Redirecting to add_product_content")
                return redirect('add_product_content', product_id=product.id)

            messages.success(request, 'Product content successfully added!')
            return redirect('product_management')
        else:
            messages.error(request, 'Form is not valid.')
    else:
        formset = ProductContentFormSet(instance=product, prefix='product_content')

    template = 'products/add_product_content.html'
    context = {
        'formset': formset,
        'product_id': product_id,
    }

    return render(request, template, context)

@staff_member_required
def edit_product(request, product_id):
    """
    Edit product info from Product model
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)

@staff_member_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('product_management'))

@staff_member_required
def add_category(request):
    """
    Add a new category
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save()
            messages.success(request, f'You successfully added category {category.friendly_name}!')
            return redirect('product_management')
        else:
            messages.error(request, 'Something went wrong, check if form is valid!')
    else:
        form = CategoryForm()

    template = 'products/add_category.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

@staff_member_required
def edit_category(request, category_id):
    """
    Edit category
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    
    category = get_object_or_404(Category, pk=category_id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated the category!')
            return redirect(reverse('product_management'))
        else:
            messages.error(
                request, 'Failed to update category. Please ensure the form is valid.')
    else:
        form = CategoryForm(instance=category)
        messages.info(request, f'You are editing {category.friendly_name}')

    template = 'products/edit_category.html'
    context = {
        'form': form,
        'category': category,
    }

    return render(request, template, context)

@staff_member_required
def delete_category(request, category_id):
    """ Delete a category from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    category = get_object_or_404(Category, pk=category_id)
    category.delete()
    messages.success(request, 'Category deleted!')
    return redirect(reverse('product_management'))