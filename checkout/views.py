from decimal import Decimal

import stripe

from django.shortcuts import render, reverse, redirect, get_object_or_404, HttpResponse
from django.db import transaction
from django.contrib import messages
from django.conf import settings

from profiles.models import UserProfile
from products.models import Product
from .forms import CheckoutForm
from .models import Order, OrderLineItem
from bag.contexts import bag_contents

stripe.api_key = settings.STRIPE_SECRET_KEY

def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if not request.user.is_authenticated:
        return redirect('login')

    order_form = CheckoutForm()

    bag = request.session.get('bag', {})
    bag_items = bag_contents(request)['bag_items']
    total = bag_contents(request)['total']
    grand_total = bag_contents(request)['grand_total']
    tax = bag_contents(request)['tax']

    user_profile = request.user.userprofile

    intent = None

    if request.method == 'POST':
        payment_method = request.POST.get('payment_option')

        if payment_method == 'card':
            order = Order.objects.create(
                user_profile=user_profile,
                order_total=total,
                grand_total=grand_total,
                tax=tax,
                payment_option='card',
            )

            for item_id, item_data in bag.items():
                try:
                    product = Product.objects.get(id=item_id)
                except Product.DoesNotExist:
                    messages.error(request, f'Product with ID {item_id} does not exist.')
                    return redirect('checkout')

                quantity = item_data['quantity']
                lineitem_total = quantity * product.price

                order_line_item = OrderLineItem(
                    order=order,
                    product=product,
                    quantity=quantity,
                    lineitem_total=lineitem_total,
                )
                order_line_item.save()

            stripe_total = round(total * 100)
            intent = stripe.PaymentIntent.create(
                amount=stripe_total,
                currency=settings.STRIPE_CURRENCY,
                return_url=request.build_absolute_uri(reverse('checkout_success', args=[order.order_number])),
            )

            try:
                intent.confirm()
            except stripe.error.CardError as e:
                messages.error(request, f'Error processing your card: {e.error.message}')
                return redirect('checkout')

            if intent.status == 'succeeded':
                messages.success(request, 'Your card payment was successful!')
                return redirect('checkout_success', order_number=order.order_number)
            else:
                # If payment fails, delete the order and line items
                order.delete()
                messages.error(request, 'Your card payment was not successful, double-check your info!')
                return redirect('checkout')

        elif payment_method == 'invoice' and 'card' == None:
            # Handle invoice payment logic here
            messages.success(request, 'Invoice payment processed successfully.')
            return redirect('order_confirmation')

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')

    template = 'checkout/checkout.html'
    context = {
        'user_profile': user_profile,
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret if intent else '',
        'bag_items': bag_items,
        'total': total,
        'grand_total': grand_total,
        'tax': tax,
    }

    return render(request, template, context)

def confirm_payment(request):
    client_secret = request.POST.get('client_secret')
    intent = stripe.PaymentIntent.retrieve(client_secret)
    
    try:
        intent.confirm()
        return JsonResponse({'status': 'succeeded'})
    except stripe.error.CardError as e:
        return JsonResponse({'status': 'failed', 'error': e.error.message})


def checkout_success(request, order_number):
    """
    Handle successful checkouts
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(request, f'Order successfully processed! \
        Your order number is. A confirmation \
        email will be sent to.')

    if 'bag' in request.session:
        del request.session['bag']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
