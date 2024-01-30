from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.forms import formset_factory
from django.http import JsonResponse

from profiles.forms import UserProfileForm
from products.models import Product
from companies.forms import CompanyForm
from .forms import CheckoutForm, ParticipantInfoForm


@login_required
def checkout(request):
    user_profile = request.user.userprofile
    existing_company = user_profile.company

    ParticipantInfoFormSet = formset_factory(ParticipantInfoForm, extra=1)

    bag_items = request.session['bag'].items()

    if request.method == 'POST':
        checkout_form = CheckoutForm(request.POST, instance=user_profile)
        company_form = CompanyForm(request.POST, instance=existing_company)
        participant_info_formset = ParticipantInfoFormSet(request.POST, prefix='participant')

        if checkout_form.is_valid() and company_form.is_valid() and participant_info_formset.is_valid():
            checkout_form.save()
            company = company_form.save(commit=False)
            user_profile.company = company
            user_profile.save()

            for item_id, quantity_data in bag_items:
                quantity = quantity_data if isinstance(quantity_data, int) else quantity_data['quantity']
                product = get_object_or_404(Product, pk=item_id)
                for i in range(quantity):
                    prefix = f'product_{item_id}_participant_{i}'
                    participant_info_form = ParticipantInfoForm(prefix=prefix)
                    participant_info = participant_info_form.save(commit=False)
                    participant_info.user = user_profile
                    participant_info.product = product
                    participant_info.save()

            if request.POST.get('save-info'):
                user_profile.save()
                company.save()

            messages.success(request, 'Your profile and company information were successfully updated!')
            return redirect('checkout')
        else:
            messages.error(request, 'Ops, something went wrong, check your details.')
    else:
        checkout_form = CheckoutForm(instance=user_profile)
        company_form = CompanyForm(instance=existing_company)
        participant_info_formsets = []

        for item_id, quantity_data in bag_items:
            quantity = quantity_data if isinstance(quantity_data, int) else quantity_data['quantity']
            product = get_object_or_404(Product, pk=item_id)

            for i in range(quantity):
                prefix = f'product_{item_id}_participant_{i}'
                participant_info_form = ParticipantInfoForm(prefix=prefix)
                participant_info = participant_info_form.save(commit=False)
                participant_info.user = user_profile
                participant_info.product = product
                participant_info.save()

            ParticipantInfoFormSet = formset_factory(ParticipantInfoForm, extra=quantity)
            participant_info_formset = ParticipantInfoFormSet(prefix=f'product_{item_id}')
            participant_info_formsets.append({'product': product, 'formset': participant_info_formset})

        return render(request, 'checkout/checkout.html', {
            'checkout_form': checkout_form,
            'company_form': company_form,
            'participant_info_formsets': participant_info_formsets,
            'bag_items': request.session['bag'],
        })

@login_required
def add_participant(request):
    response_data = {'success': False, 'message': 'Error adding participant'}

    if request.method == 'POST':
        participant_info_form = ParticipantInfoForm(request.POST)
        if participant_info_form.is_valid():
            participant_info = participant_info_form.save(commit=False)
            participant_info.user = request.user
            participant_info.product = Product.objects.get(pk=request.POST['product_id'])
            participant_info.save()

            response_data['success'] = True
            response_data['message'] = 'Participant successfully added'
            return JsonResponse(response_data)

    response_data['message'] = 'Error adding participant. Please check your data.'
    return JsonResponse(response_data)