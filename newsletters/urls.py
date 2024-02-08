from django.urls import path
from . import views


urlpatterns = [
    path('create/', views.create_newsletter, name='create_newsletter'),
    path('', views.newsletters, name='newsletters'),
]