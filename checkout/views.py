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
from .forms import CheckoutForm, ParticipantInfoForm
from .models import Order, OrderLineItem, Participant
from bag.contexts import bag_contents


def process_bag_items(order, bag):
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

                formset_key = f'product_{item_id}'
                participant_info_formset = order.participant_info_formsets.get(formset_key, None)
                if participant_info_formset:
                    for participant_info_form in participant_info_formset:
                        if participant_info_form.is_valid():
                            participant = participant_info_form.save(commit=False)
                            participant.order_line_item = order_line_item
                            participant.save()
        except Product.DoesNotExist:
            messages.error(request, (
                "One of the products in your bag wasn't found in our database. "
                "Please call us for assistance!")
            )
            order.delete()
            return redirect(reverse('view_bag'))


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == 'POST':
        bag = request.session.get('bag', {})
        form_data = {
            'first_name': request.POST['first_name'],
            'last_name': request.POST['last_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'company_name': request.POST['company_name'],
            'org_num': request.POST['org_num'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'postcode': request.POST['postcode'],
            'city': request.POST['city'],
            'country': request.POST['country'],
        }
        order_form = CheckoutForm(request.user, form_data)

        if order_form.is_valid():
            order = order_form.save()
            process_bag_items(order, bag)

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success', args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with your form. \
                Please double-check your information.')
    else:
        bag = request.session.get('bag', {})
        if not bag:
            messages.error(request, "There's nothing in your bag at the moment")
            return redirect(reverse('products'))

        current_bag = bag_contents(request)
        total = current_bag['grand_total'] + current_bag['tax']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        order_form = CheckoutForm(user=request.user)

        participant_info_formsets = []

        total_items = current_bag['bag_items']

        bag_total = sum(item['product'].price * item['quantity'] for item in total_items)

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'participant_info_formsets': participant_info_formsets,
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
