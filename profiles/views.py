from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import UserProfileForm
from companies.forms import CompanyForm
from companies.models import Company  # Import the Company model


@login_required
def profile(request):
    user_profile = request.user.userprofile
    existing_company = user_profile.company

    profile_form = UserProfileForm(instance=user_profile)
    company_form = CompanyForm(instance=existing_company)

    if request.method == 'POST':
        if 'profile-update-form' in request.POST:
            profile_form = UserProfileForm(request.POST, instance=user_profile)
            if profile_form.is_valid():
                profile_form.save()
                messages.success(request, 'Your profile was successfully updated!')
            else:
                messages.error(request, 'Ops, something went wrong with your profile, check your details.')

        elif 'company-update-form' in request.POST:
            # Use CompanyForm from companies/forms.py
            company_form = CompanyForm(request.POST, instance=existing_company)
            if company_form.is_valid():
                company_form.save()
                messages.success(request, 'Your company information was successfully updated!')
            else:
                messages.error(request, 'Ops, something went wrong with your company information, check your details.')

        # Query the user_profile and existing_company again to get the updated information
        user_profile = request.user.userprofile
        existing_company = user_profile.company

        # Update the forms with the new instances
        profile_form = UserProfileForm(instance=user_profile)
        company_form = CompanyForm(instance=existing_company)

    return render(request, 'profiles/profile.html', {'profile_form': profile_form, 'company_form': company_form})

