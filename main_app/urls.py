
from django.urls import path
from main_app.views import index, contact

urlpatterns = [
    path('',index, name='home_page'),
    path('contact',contact, name='contact_page'),
]
