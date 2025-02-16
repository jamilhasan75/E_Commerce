
from django.urls import path
from main_app.views import *

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',index, name='home_page'),
    path('contact/',contact, name='contact_page'),
    path('about/', about, name='about_page'),

    path('product_detail/<int:pk>/', product_detail,name='product_detail'),
    path('search/', product_search, name='product_search_page'),
    path('categories_product/<int:pk>', categories_product, name='categories_product_page'),

    path('add_to_cart/<int:product_id>', add_to_cart, name='add_to_cart'),
    path('increment/<int:item_id>', increment_cart_item, name='increment_cart_item'),
    path('decrement/<int:item_id>', decrement_cart_item, name='decrement_cart_item'),

    path('cart/', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),

    path('add_to_wishlist/<int:product_id>', add_to_wishlist, name='add_to_wishlist'),
    path('wishlist/', wishlist, name='wishlist'),

    path('payment/<int:order_id>/', payment, name='payment'),
    path('order_confirmation/<int:order_id>/', order_confirmation, name='order_confirmation'),
    path('order_history/', order_history, name='order_history'),

    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='user_app/passwordchange.html'), name='password-change'),
    path('password_change/done', auth_views.PasswordChangeDoneView.as_view(template_name='user_app/passwordchange_done.html'), name='password_change_done'),
]
