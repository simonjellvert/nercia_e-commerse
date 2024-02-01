from django.urls import path
from . import views
from allauth.account.views import SignupView
from .forms import CustomSignupForm

urlpatterns = [
    path('', views.profile, name='profile'),
    path('accounts/signup/', SignupView.as_view(form_class=CustomSignupForm), name='account_signup'),
]
