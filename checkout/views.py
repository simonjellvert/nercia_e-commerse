from decimal import Decimal

import stripe

from django.shortcuts import render, reverse, redirect, get_object_or_404, HttpResponse
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

from profiles.models import UserProfile
from products.models import Product
from .forms import CheckoutForm
from .models import Order, OrderLineItem
from bag.contexts import bag_contents


@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'bag': json.dumps(request.session.get('bag', {})),
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, you payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)

stripe.api_key = settings.STRIPE_SECRET_KEY

@login_required
def checkout(request):
    """
    Function to handle invoice or card payment
    """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    bag_context = bag_contents(request)
    bag_items = bag_context['bag_items']
    total = bag_context['total']
    grand_total = bag_context['grand_total']
    tax = bag_context['tax']

    user_profile = request.user.userprofile

    intent = stripe.PaymentIntent.create(
        amount=round(grand_total * 100),
        currency=settings.STRIPE_CURRENCY,
    )

    if request.method == 'POST':
        order_form = CheckoutForm(request.POST)
        payment_method = request.POST.get('payment_option')

        if order_form.is_valid():
            if payment_method == 'card':
                # Handle card payment logic here
                order = Order.objects.create(
                    user_profile=user_profile,
                    order_total=total,
                    grand_total=grand_total,
                    tax=tax,
                    payment_option='card',
                )

                for item_data in bag_context['bag_items']:
                    item_id = item_data['item_id']
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

                    bag_items = bag_context['bag_items']

                    messages.success(request, 'Your card payment was successful!')
                    return redirect('checkout_success', order_number=order.order_number)
                else:
                    messages.error(request, 'Your card payment was not successful, double-check your info!')
                    return redirect('checkout')

            elif payment_method == 'invoice':
                # Handle invoice payment logic here
                order_form = CheckoutForm(request.POST)
                if order_form.is_valid():
                    invoice_ref = order_form.cleaned_data.get('invoice_ref')

                    if not invoice_ref:
                        messages.error(request, 'Please enter the invoice reference.')
                        return redirect('checkout')

                    order = Order.objects.create(
                        user_profile=user_profile,
                        order_total=total,
                        grand_total=grand_total,
                        tax=tax,
                        payment_option='invoice',
                        invoice_ref=invoice_ref
                    )

                    for item_data in bag_context['bag_items']:
                        item_id = item_data['item_id']
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
                        
                        bag_items = bag_context['bag_items']

                    messages.success(request, 'Invoice payment processed successfully.')
                    return redirect('checkout_success', order_number=order.order_number)

                else:
                    messages.error(request, 'Invalid payment method selected.')
                    return redirect('checkout')
        else:
            messages.error(request, 'There are errors in your form. Please correct them and try again.')
            return redirect('checkout')
    else:
        order_form = CheckoutForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')

    template = 'checkout/checkout.html'
    context = {
        'user_profile': user_profile,
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
        'bag_items': bag_items,
        'total': total,
        'grand_total': grand_total,
        'tax': tax,
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    """
    Handle successful checkouts
    """
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.user_profile.user.email}.')

    bag_context = bag_contents(request)
    bag_items = bag_context['bag_items']

    if 'bag' in request.session:
        del request.session['bag']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'bag_items': bag_items,
        'user_profile': order.user_profile,
    }

    return render(request, template, context)
