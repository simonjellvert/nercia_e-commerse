from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import UserProfile

def profile(request):
    if request.method == 'POST':
        form = YourSignupForm(request.POST)
        if form.is_valid():
            # Your form processing logic here
            messages.success(request, 'User created successfully')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = YourSignupForm()

    template = 'profiles/profile.html'
    context = {'form': form}
    return render(request, template, context)