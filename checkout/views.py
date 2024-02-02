from decimal import Decimal

import stripe

from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.db import transaction
from django.contrib import messages
from django.forms.models import inlineformset_factory
from django.http import JsonResponse
from django.conf import settings

from profiles.forms import UserProfileForm
from profiles.models import UserProfile
from products.models import Product
from .forms import CheckoutForm
from .models import Order, OrderLineItem
from bag.contexts import bag_contents


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if not request.user.is_authenticated:
        return redirect('login')

    # Create a dictionary with user information
    user_info = {
        'first_name': '', 'last_name': '', 'email': '', 'phone_number': '',
        'company_name': '', 'org_num': '', 'street_address1': '',
        'street_address2': '', 'postcode': '', 'city': '',
        'country': '', 'invoice_email': ''
    }
    
    user_profile = request.user.userprofile
    order_form = CheckoutForm()
    grand_total += item_data * product.price
    bag_total = []
    total_items = []
    intent = None

    if request.method == 'POST':
        print("Inside POST request")
        bag = request.session.get('bag', {})
        form_data = {
            'first_name': user_profile.first_name,
            'last_name': user_profile.last_name,
            'email': user_profile.email,
            'phone_number': user_profile.phone_number,
            'company_name': user_profile.company_name,
            'org_num': user_profile.org_num,
            'street_address1': user_profile.street_address1,
            'street_address2': user_profile.street_address2,
            'postcode': user_profile.postcode,
            'city': user_profile.city,
            'country': user_profile.country,
            'invoice_email': user_profile.invoice_email,
        }
        order_form = CheckoutForm(form_data)
        print("Form errors (before validation):", order_form.errors)

        if order_form.is_valid():
            print("Form is valid")
            order = order_form.save(commit=False)
            order.user_profile = request.user.userprofile
            order.save()

            for item_id, item_data in bag.items():
                try:
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_line_item.save()
                except Product.DoesNotExist:
                    messages.error(request, "Product not found. Please call for assistance.")
                    order.delete()
                    return redirect(reverse('view_bag'))

            order.update_total()

            intent = stripe.PaymentIntent.create(
                amount=stripe_total,
                currency=settings.STRIPE_CURRENCY,
            )

            print(f"Order successfully created! Order number: {order.order_number}")
            print(f"Total amount: {order.grand_total}")
            print(f"Payment option: {order.payment_option}")

            return redirect(reverse('checkout_success', args=[order.order_number]))

    else:
        print("Form is NOT valid")
        print("Form errors:", order_form.errors)
        bag = request.session.get('bag', {})
        if not bag:
            messages.error(request, "There's nothing in your bag at the moment")
            return redirect(reverse('products'))

        current_bag = bag_contents(request)
        tax = grand_total * 0.25
        total = current_bag['grand_total'] + current_bag['tax']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        grand_total = 0
        for item_id, item_data in bag.items():
            try:
                product = Product.objects.get(id=item_id)
                if isinstance(item_data, int):
                    grand_total += item_data * product.price
            except Product.DoesNotExist:
                messages.error(request, "Product not found. Please call for assistance.")
                return redirect(reverse('view_bag'))

        order_form = CheckoutForm()
        bag_total = current_bag['grand_total']
        total_items = current_bag['bag_items']

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')

    template = 'checkout/checkout.html'
    context = {
        'user_profile': user_profile,
        'user_info': user_info,
        'order_form': order_form,
        'bag_items': total_items,
        'bag_total': bag_total,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    """
    Handle successful checkouts
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')

    if 'bag' in request.session:
        del request.session['bag']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
