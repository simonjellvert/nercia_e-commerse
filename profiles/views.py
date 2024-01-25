from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import UserProfile
import logging

logger = logging.getLogger(__name__)

def profile(request):
    """
    Display users profile
    """
    print(f"Requested user: {request.user}")
    try:
        profile = get_object_or_404(UserProfile, user=request.user)
    except UserProfile.DoesNotExist:
        logger.warning(f"No UserProfile found for user {request.user}")
        raise

    template = 'profiles/profile.html'
    context = {'profile': profile}
    return render(request, template, context)
