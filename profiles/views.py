from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import UserProfile
from .forms import UserProfileForm, CompanyForm


def profile(request):
    """
    Display users profile
    """
    
    profile = get_object_or_404(UserProfile, user=request.user)
    user_profile_form = UserProfileForm()
    company_form = CompanyForm()

    if request.method == 'POST':
        user_profile_form = UserProfileForm(request.POST, instance=profile)
        company_form = CompanyForm(request.POST)
        
        if user_profile_form.is_valid() and company_form.is_valid():
            user_profile_form.save()
            company = company_form.save(commit=False)
            company.user_profile = profile
            company.save()
            
            messages.success(request, 'Profile updated successfully!')
            return redirect('your_redirect_url')

    else:
        user_profile_form = UserProfileForm(instance=profile)
        company_form = CompanyForm()

    template = 'profiles/profile.html'
    context = {
        'profile': profile,
        'user_profile_form': user_profile_form,
        'company_form': company_form
    }

    return render(request, template, context)
