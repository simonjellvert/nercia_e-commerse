from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import CheckoutForm

def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There is noting in your bag right now!")
        return redirect(reverse('products'))

    checkout_form = CheckoutForm()
    template = 'checkout/checkout.html'
    context = {
        'checkout_form': checkout_form,
    }

    return render(request, template, context)
