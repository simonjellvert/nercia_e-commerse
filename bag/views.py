from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import Product


def view_bag(request):
    """
    A view to return the shopping bag
    """

    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):
    """
    A view to add quantity of a product to the bag
    """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity', 1))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
        messages.success(request, f'Updated {product.name} quantity to {bag[item_id]}')
    else:
        bag[item_id] = quantity
        messages.success(request, f'Added {product.name} to your bag')
    
    request.session['bag'] = bag
    return redirect(redirect_url)


def edit_bag(request, item_id):
    """
    A view to edit quantity of a product to the bag
    """
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
        messages.success(request, f'Updated {product.name} quantity to {bag[item_id]}')
    else:
        bag.pop(item_id)
        messages.success(request, f'Deleted {product.name} from your bag')
    
    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def delete_item(request, item_id):
    """
    A view to delete item of a product to the bag
    """
    product = get_object_or_404(Product, pk=item_id)
    bag = request.session.get('bag', {})

    try:
        if item_id in bag:
            bag.pop(item_id)
            messages.success(request, f'Deleted {product.name} from your bag')
        
        request.session['bag'] = bag
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, f'Error when deleting item: {e}')
        return HttpResponse(status=500)
