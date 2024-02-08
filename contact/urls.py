from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact, name='contact'),
    path('add_contact/', views.add_contact, name='add_contact'),
    path('edit_contact/', views.edit_contact, name='edit_contact'),
    path('delete_contact/', views.delete_contact, name='delete_contact'),
]
