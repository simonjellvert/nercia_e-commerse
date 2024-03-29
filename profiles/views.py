from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from allauth.account.views import SignupView

from .forms import CustomSignupForm, UserProfileForm, DeleteAccountForm
from .models import UserProfile
from checkout.models import Order


class CustomSignUpView(SignupView):
    """ Sets up custom signup view """
    form_class = CustomSignupForm


@login_required
def profile(request):
    """ A view for profile page """
    try:
        user_profile = request.user.userprofile
    except UserProfile.DoesNotExist:
        user_profile, created = UserProfile.objects.get_or_create(
            user=request.user
        )

    orders = user_profile.orders.all()

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
                messages.success(
                    request,
                    'Your profile was successfully updated!'
                )
            else:
                messages.error(
                    request,
                    'Ops, something went wrong with your profile, '
                    'check your details.')

        user_profile = request.user.userprofile
        profile_form = UserProfileForm(instance=user_profile)

    return render(
        request,
        'profiles/profile.html', {
            'profile_form': profile_form,
            'orders': orders,
            'user_profile': user_profile
        }
    )


def order_history(request, order_number):
    """ View for viewing order hostiry """
    order = get_object_or_404(Order, order_number=order_number)
    user_profile = request.user.userprofile
    bag_items = order.lineitems.all()

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A conformation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'user_profile': user_profile,
        'from_profile': True,
        'bag_items': bag_items,
    }

    return render(request, template, context)


@login_required
def delete_profile(request, user_profile_id):
    """ Function to delete profile """
    user_profile = UserProfile.objects.get(pk=user_profile_id)

    if request.method == 'POST':
        form = DeleteAccountForm(request.POST)

        if form.is_valid():
            password = form.cleaned_data['password']

            user = authenticate(email=request.user.email, password=password)

            if user is not None:
                # Check if the user to be deleted is the logged-in user
                if user.id == user_profile.user.id:
                    user_profile.user.delete()
                    logout(request)
                    messages.success(request, 'Account deleted successfully!')
                    return redirect(reverse('home'))
                else:
                    messages.error(
                        request,
                        'You can only delete your own account.'
                    )
            else:
                messages.error(
                    request,
                    'Incorrect password. Account not deleted.'
                )
    else:
        form = DeleteAccountForm()

    template = 'profiles/delete_profile.html'
    context = {
        'user_profile': user_profile,
        'form': form,
    }

    return render(request, template, context)
