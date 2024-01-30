from decimal import Decimal

from django.conf import settings
from django.shortcuts import get_object_or_404

from products.models import Product


def bag_contents(request):
    """
    A context processor to use bag information across all templates
    """
    bag_items = []
    total = 0
    product_count = 0
    grand_total = 0
    tax = 0
    bag = request.session.get('bag', {})
    print("Bag in bag_contents:", bag)

    for item_id, item_data in bag.items():
        if isinstance(item_data, int):
            # Handle the case where item_data is an integer
            product = get_object_or_404(Product, pk=item_id)
            item_total = item_data * product.price
            grand_total += item_total
            product_count += item_data
            bag_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
                'item_total': item_total,
            })
        else:
            # Handle the case where item_data is a dictionary
            product = get_object_or_404(Product, pk=item_id)
            item_total = item_data['quantity'] * product.price
            grand_total += item_total
            product_count += item_data['quantity']
            bag_items.append({
                'item_id': item_id,
                'quantity': item_data['quantity'],
                'product': product,
                'item_total': item_total,
            })

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'grand_total': grand_total,
        'tax': tax,
    }

    return context