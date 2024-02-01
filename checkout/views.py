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
                        participant_info_formset = order_form.participant_info_formsets.get(f'product_{item_id}', None)
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

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success', args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')
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

# @transaction.atomic
# def checkout(request):
#     stripe_public_key = settings.STRIPE_PUBLIC_KEY
#     stripe_secret_key = settings.STRIPE_SECRET_KEY

#     user_profile = request.user.userprofile
#     existing_company = user_profile.company

#     ParticipantInfoFormSet = inlineformset_factory(Product, Participant, form=ParticipantInfoForm, extra=1, can_delete=False)

#     bag_items = request.session['bag']
#     total_items = []
#     bag_total = 0
#     tax = Decimal(0)
#     promo_code = 0

#     user = request.user
#     company = user.userprofile.company if user.userprofile else None

#     checkout_form = CheckoutForm(instance=user_profile)
#     company_form = CompanyForm(instance=existing_company)

#     participant_info_formsets = []

#     order_instance = None

#     for item_id, quantity_data in bag_items.items():
#         product = get_object_or_404(Product, pk=item_id)
#         quantity = quantity_data['quantity']

#         participant_info_formset = ParticipantInfoFormSet(prefix=f'product_{item_id}')

#         participant_info_formset.product = product
#         participant_info_formset.quantity = quantity

#         for _ in range(quantity):
#             participant_info_formsets.append(participant_info_formset)

#         product_price_total = product.price * quantity

#         total_items.append({
#             'product_name': product.name,
#             'quantity': quantity,
#             'product_price_total': product_price_total,
#         })

#         bag_total += product_price_total

#     grand_total = bag_total - promo_code
#     tax = Decimal(grand_total) * Decimal(0.25)

#     stripe_total = round((grand_total + tax) * 100)
#     stripe.api_key = stripe_secret_key
#     intent = stripe.PaymentIntent.create(
#         amount=stripe_total,
#         currency=settings.STRIPE_CURRENCY,
#     )

#     if request.method == 'POST':
#         print(request.POST)
#         user_profile_instance, created = UserProfile.objects.get_or_create(user=request.user)
#         checkout_form = CheckoutForm(request.POST, instance=order_instance)
#         checkout_form.fields['user_profile'].initial = user_profile_instance
#         company_form = CompanyForm(request.POST)

#         participant_info_formsets = []
    
#         order_instance = checkout_form.save(commit=False)
#         order_instance.user_profile = user_profile_instance
#         order_instance.save()

#         checkout_form.instance.user_profile = user_profile_instance
#         checkout_form.instance.company = company_instance
#         checkout_form.save()

#         if checkout_form.is_valid() and company_form.is_valid():

#             checkout_form.instance.user_profile = user_profile_instance
#             checkout_form.instance.order_total = bag_total
#             checkout_form.instance.grand_total = grand_total
#             checkout_form.instance.tax = tax
#             checkout_form.instance.company = company
#             checkout_form.save()

#             for item_id, quantity_data in bag_items.items():
#                 product = get_object_or_404(Product, pk=item_id)
#                 participant_info_formset = ParticipantInfoFormSet(
#                     request.POST, prefix=f'product_{item_id}', instance=order_instance)
                
#                 if participant_info_formset.is_valid():
#                     for form in participant_info_formset:
#                         if form.cleaned_data:
#                             participant = form.save(commit=False)
#                             participant.product = product
#                             participant.order = order_instance
#                             participant.save()
#                 else:
#                     messages.error(request, 'Invalid participant information.')
#                     return redirect('checkout')
                    
#             return redirect('checkout_success', order_number=order_instance.order_number)
#         else:
#             messages.error(request, 'Invalid form submission.')

#     return render(request, 'checkout/checkout.html', {
#         'checkout_form': checkout_form,
#         'company_form': company_form,
#         'participant_info_formsets': participant_info_formsets,
#         'bag_items': total_items,
#         'bag_total': bag_total,
#         'tax': tax,
#         'stripe_public_key': stripe_public_key,
#         'client_secret': intent.client_secret,
#     })

# def checkout_success(request, order_number):
#     """
#     Handle successful checkouts
#     """
#     save_info = request.session.get('save_info')
#     order = get_object_or_404(Order, order_number=order_number)
#     messages.success(request, f'Order successfully processed! \
#         Your order number is {order_number}. A confirmation \
#         email will be sent to {order.email}.')

#     if 'bag' in request.session:
#         del request.session['bag']

#     template = 'checkout/checkout_success.html'
#     context = {
#         'order': order,
#     }

#     return render(request, template, context)