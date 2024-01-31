from django.urls import path
from .views import checkout, checkout_success

urlpatterns = [
    path('', checkout, name='checkout'),
    path('checkout_success/<order_number>', checkout_success, name='checkout_success'),
]
