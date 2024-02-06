from django.urls import path
from . import views
from allauth.account.views import SignupView
from .forms import CustomSignupForm, DeleteAccountForm

urlpatterns = [
    path('', views.profile, name='profile'),
    path('accounts/signup/', SignupView.as_view(form_class=CustomSignupForm), name='account_signup'),
    path('order_history/<order_number>/', views.order_history, name='order_history'),
    path('delete/<int:user_profile_id>/', views.delete_profile, name='delete_profile'),
]
