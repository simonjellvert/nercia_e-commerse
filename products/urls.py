from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('products/manage/', views.product_management, name='product_management'),
    path('add/', views.add_product, name='add_product'),
    path('addcontent/<int:product_id>/', views.add_product_content, name='add_product_content'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
]
