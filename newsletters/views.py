from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.conf import settings
from django.core.mail import send_mail

from .forms import NewsletterForm
from .models import Newsletter
from profiles.models import UserProfile


@staff_member_required
def newsletters(request):
    """
    A view for the administrator to see a list of previous newsletters, categorized
    """
    newsletters_list = Newsletter.objects.all().order_by('-created_at')
    if 'newsletter_category' in request.GET:
        category = request.GET['newsletter_category']
        if category:
            newsletters_list = newsletters_list.filter(newsletter_category=category)

    template = 'newsletters/newsletters.html'
    context = {
        'newsletters_list': newsletters_list,
    }
    
    return render(request, template, context)


@staff_member_required
def create_newsletter(request):
    """
    View to create a newsletter
    """
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            newsletter = form.save()
            user_profiles = UserProfile.objects.filter(newsletter_subscription=True)
            recipients = [user_profile.user.email for user_profile in user_profiles]
            subject = newsletter.title
            message = newsletter.content
            from_email = settings.DEFAULT_FROM_EMAIL
            send_mail(subject, message, from_email, recipients, fail_silently=True)
            messages.success(request, 'Newsletter created successfully!')
            return redirect('newsletters')
        else:
            form = NewsletterForm()
            messages.error(request, 'Something went wrong, check your form and try again!')
    else:
        form = NewsletterForm()
    
    template = 'newsletters/create_newsletter.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
