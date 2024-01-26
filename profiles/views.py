from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import get_user_model

from .models import UserProfile
from .forms import UserProfileForm
from companies.forms import CompanyForm
from companies.models import Company


def profile(request):
    """
    Display users profile
    """

    print("Type of request.user:", type(request.user))
    print("Request user:", request.user)
    
    profile = get_object_or_404(UserProfile, user=request.user)
    
    # Fetch the associated company for the current user
    user_company = get_object_or_404(Company, userprofile=profile)

    user_profile_form = UserProfileForm(instance=profile)
    company_form = CompanyForm(instance=user_company)

    if request.method == 'POST':
        user_profile_form = UserProfileForm(request.POST, instance=profile)
        company_form = CompanyForm(request.POST, instance=user_company)

        if user_profile_form.is_valid() and company_form.is_valid():
            print("User Profile Form Data:", user_profile_form.cleaned_data)
            print("Company Form Data:", company_form.cleaned_data)
            user_profile_form.save()
            company_form.save()

            messages.success(request, 'Profile updated successfully!')
            profile = get_object_or_404(UserProfile, user=request.user)
            user_profile_form = UserProfileForm(instance=profile)

            return render(request, 'profiles/profile.html', {'profile': profile, 'user_profile_form': user_profile_form, 'company_form': company_form})

        else:
            messages.error(request, 'There was an error with the form submission. Please check your data.')

    template = 'profiles/profile.html'
    context = {
        'profile': profile,
        'user_profile_form': user_profile_form,
        'company_form': company_form
    }

    return render(request, template, context)
