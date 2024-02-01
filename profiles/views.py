from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import UserProfileForm


@login_required
def profile(request):
    user_profile = request.user.userprofile

    profile_form = UserProfileForm(instance=user_profile)

    if request.method == 'POST':
        if 'profile-update-form' in request.POST:
            profile_form = UserProfileForm(request.POST, instance=user_profile)
            if profile_form.is_valid():
                profile_form.save()
                messages.success(request, 'Your profile was successfully updated!')
            else:
                messages.error(request, 'Ops, something went wrong with your profile, check your details.')

        user_profile = request.user.userprofile
        profile_form = UserProfileForm(instance=user_profile)

    return render(request, 'profiles/profile.html', {'profile_form': profile_form})

