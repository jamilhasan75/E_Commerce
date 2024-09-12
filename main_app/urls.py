
from django.urls import path
from main_app.views import *

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',index, name='home_page'),
    path('contact/',contact, name='contact_page'),
    path('product_detail/<int:pk>/', product_detail,name='product_detail'),
    path('about/', about, name='about_page'),
    path('search/', product_search, name='product_search_page'),
    path('categories_product/<int:pk>', categories_product, name='categories_product_page'),
    path('add_to_cart/<int:product_id>', add_to_cart, name='add_to_cart'),
    path('add_to_wishlist/<int:product_id>', add_to_wishlist, name='add_to_wishlist'),
    path('cart/', cart, name='cart'),
    path('wishlist', wishlist, name='wishlist'),

    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='user_app/passwordchange.html'), name='password-change'),
    path('password_change/done', auth_views.PasswordChangeDoneView.as_view(template_name='user_app/passwordchange_done.html'), name='password_change_done'),
]
