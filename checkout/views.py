from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from profiles.forms import UserProfileForm
from products.models import Product
from companies.forms import CompanyForm
from .forms import CheckoutForm, ParticipantInfoForm


@login_required
def checkout(request):
    user_profile = request.user.userprofile
    existing_company = user_profile.company

    if request.method == 'POST':
        checkout_form = CheckoutForm(request.POST, instance=user_profile)
        company_form = CompanyForm(request.POST, instance=existing_company)

        if checkout_form.is_valid() and company_form.is_valid():
            checkout_form.save()
            company = company_form.save(commit=False)
            user_profile.company = company
            user_profile.save()

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
    
    participant_info_form = ParticipantInfoForm()
    bag = request.session.get('bag', {})

    return render(request, 'checkout/checkout.html', {'checkout_form': checkout_form, 'company_form': company_form})
