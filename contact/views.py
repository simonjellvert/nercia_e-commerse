from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required

from .forms import ContactForm
from .models import Contact


def contact(request):
    """
    A view to return contact page
    """
    contacts = Contact.objects.all()
    
    return render(request, 'contact/contact.html', {'contacts': contacts})

@staff_member_required
def add_contact(request):
    """
    Add contact view
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            contact = form.save()
            messages.success(request, f'You successfully added {contact.name}!')
            return redirect('contact')
        else:
            messages.error(request, 'Something went wrong, check if form is valid!')
    else:
        form = ContactForm()

    template = 'contact/contact.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

@staff_member_required
def edit_contact(request, contact_id):
    """
    Edit contact view
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    
    contact = get_object_or_404(Contact, pk=contact_id)
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES, instance=contact)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated contact!')
            return redirect(reverse('contact', args=[contact.id]))
        else:
            messages.error(
                request, 'Failed to update contact. Please ensure the form is valid.')
    else:
        form = ContactForm(instance=contact)
        messages.info(request, f'You are editing {contact.name}')

    template = 'contact/contact.html'
    context = {
        'form': form,
        'contact': contact,
    }

    return render(request, template, context)

@staff_member_required
def delete_contact(request, contact_id):
    """
    Delete a contact
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    contact = get_object_or_404(Contact, pk=contact_id)
    contact.delete()
    messages.success(request, 'Contact deleted!')
    return redirect(reverse('contact'))
