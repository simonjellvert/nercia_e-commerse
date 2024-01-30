from django.urls import path
from .views import checkout, add_participant

urlpatterns = [
    path('', checkout, name='checkout'),
    path('add_participant/', add_participant, name='add_participant'),
]
