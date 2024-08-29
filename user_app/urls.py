from django.urls import path

from .views import *
urlpatterns = [
    path('register/',register, name='register'),
    path('login/',login, name='login'),
    path('logout/',logout_view, name='logout_view'),
    path('profile/',profile,name='profile-page'),
    path('profile/update/',profileupdate,name='profileupdate-page'),
]
