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
from companies.models import Company
from companies.forms import CompanyForm
from .forms import CheckoutForm, ParticipantInfoForm
from .models import Order, OrderLineItem, Participant
from bag.contexts import bag_contents


@transaction.atomic
def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    user_profile = request.user.userprofile
    existing_company = user_profile.company

    ParticipantInfoFormSet = inlineformset_factory(Product, Participant, form=ParticipantInfoForm, extra=1, can_delete=False)

    bag_items = request.session['bag']
    total_items = []
    bag_total = 0
    tax = Decimal(0)
    promo_code = 0

    checkout_form = CheckoutForm(instance=user_profile)
    company_form = CompanyForm(instance=existing_company)

    participant_info_formsets = []

    order_instance = None  # Initialize order_instance

    for item_id, quantity_data in bag_items.items():
        product = get_object_or_404(Product, pk=item_id)
        quantity = quantity_data['quantity']

        # Initialize ParticipantInfoFormSet for each product
        participant_info_formset = ParticipantInfoFormSet(prefix=f'product_{item_id}')

        # Attach the product and quantity to the formset
        participant_info_formset.product = product
        participant_info_formset.quantity = quantity

        # Create the correct number of formsets based on quantity
        for _ in range(quantity):
            participant_info_formsets.append(participant_info_formset)

        product_price_total = product.price * quantity

        total_items.append({
            'product_name': product.name,
            'quantity': quantity,
            'product_price_total': product_price_total,
        })

        bag_total += product_price_total

    grand_total = bag_total - promo_code
    tax = Decimal(grand_total) * Decimal(0.25)

    stripe_total = round((grand_total + tax) * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    if request.method == 'POST':
        print("Received POST request")
        print(request.POST)
        user_profile_instance, created = UserProfile.objects.get_or_create(user=request.user)
        print(f"User Profile Instance: {user_profile_instance}")
        checkout_form = CheckoutForm(request.POST, instance=order_instance)
        print(f"Checkout Form: {checkout_form}")
        checkout_form.fields['user_profile'].initial = user_profile_instance
        company_form = CompanyForm(request.POST)

        participant_info_formsets = []
    
        # New order_instance should be created here
        order_instance = checkout_form.save(commit=False)
        order_instance.user_profile = user_profile_instance
        order_instance.save()

        if checkout_form.is_valid() and company_form.is_valid():
            # Process checkout form 
            print("Forms are valid")

            checkout_form.instance.user_profile = user_profile_instance
            checkout_form.instance.order_total = bag_total
            checkout_form.instance.grand_total = grand_total
            checkout_form.instance.tax = tax
            checkout_form.instance.company_name = new_company  # Assign the new company to order_instance
            checkout_form.save()

            # Process participant info formsets for each product
            for item_id, quantity_data in bag_items.items():
                product = get_object_or_404(Product, pk=item_id)
                participant_info_formset = ParticipantInfoFormSet(request.POST, prefix=f'product_{item_id}', instance=order_instance)
                
                if participant_info_formset.is_valid():
                    for form in participant_info_formset:
                        if form.cleaned_data:
                            participant = form.save(commit=False)
                            participant.product = product
                            participant.order = order_instance
                            participant.save()
                else:
                    messages.error(request, 'Invalid participant information.')
                    return redirect('checkout')
                    
            return redirect('checkout_success', order_number=order_instance.order_number)
        else:
            print("Forms are NOT valid")
            print(checkout_form.errors)
            print(company_form.errors)
            messages.error(request, 'Invalid form submission.')

    return render(request, 'checkout/checkout.html', {
        'checkout_form': checkout_form,
        'company_form': company_form,
        'participant_info_formsets': participant_info_formsets,
        'bag_items': total_items,
        'bag_total': bag_total,
        'tax': tax,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    })

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