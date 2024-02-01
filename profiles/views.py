from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from allauth.account.views import SignupView
from .forms import CustomSignupForm

from .forms import UserProfileForm


class CustomSignUpView(SignupView):
    form_class = CustomSignupForm


@login_required
def profile(request):
    user_profile = request.user.userprofile

    initial_data = {
        'first_name': user_profile.first_name,
        'last_name': user_profile.last_name,
        'email': request.user.email,
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

    profile_form = UserProfileForm(instance=user_profile, initial=initial_data)

    if request.method == 'POST':
        if 'profile-update-form' in request.POST:
            profile_form = UserProfileForm(request.POST, instance=user_profile)
            if profile_form.is_valid():
                profile_form.save()
                messages.success(request, 'Your profile was successfully updated!')
            else:
                print("Form errors:", profile_form.errors)
                messages.error(request, 'Ops, something went wrong with your profile, check your details.')

        user_profile = request.user.userprofile
        profile_form = UserProfileForm(instance=user_profile)

    return render(request, 'profiles/profile.html', {'profile_form': profile_form})
