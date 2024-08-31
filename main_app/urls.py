
from django.urls import path
from main_app.views import index, contact, product_detail, about

urlpatterns = [
    path('',index, name='home_page'),
    path('contact/',contact, name='contact_page'),
    path('product_detail/<int:pk>/', product_detail,name='product_detail'),
    path('about/', about, name='about_page'),
]
