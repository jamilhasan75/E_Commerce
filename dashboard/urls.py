
from django.urls import path
from dashboard.views import *

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('dashboard/',index, name='index'),
    path('product_list/',product_list, name='product_list'),
    
]
