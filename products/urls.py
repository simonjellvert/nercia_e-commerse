from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path(
        '<int:product_id>/',
        views.product_detail,
        name='product_detail'
    ),
    path(
        'products/manage/',
        views.product_management,
        name='product_management'
    ),
    path(
        'add/',
        views.add_product,
        name='add_product'
    ),
    path(
        'addcontent/<int:product_id>/',
        views.add_product_content,
        name='add_product_content'
    ),
    path(
        'edit/<int:product_id>/',
        views.edit_product,
        name='edit_product'
    ),
    path(
        'editcontent/<int:product_id>/',
        views.edit_product_content,
        name='edit_product_content'
    ),
    path(
        'delete/<int:product_id>/',
        views.delete_product,
        name='delete_product'
    ),
    path(
        'add/category/',
        views.add_category,
        name='add_category'
    ),
    path(
        'edit/category/<int:category_id>/',
        views.edit_category,
        name='edit_category'
    ),
    path(
        'delete/category/<int:category_id>/',
        views.delete_category,
        name='delete_category'
    ),
]
