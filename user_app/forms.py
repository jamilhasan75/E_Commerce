from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import *
from django.core.exceptions import ValidationError

class RegistrationForm(UserCreationForm):
       class Meta:
        model = User 
        fields = ['first_name','last_name','username','email','password1','password2']
        
        
        
class UserUpdate(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email','username',]        
        
        
        
class ProfileUpdate(forms.ModelForm):
    Date_of_Birth = forms.DateField(required=False,
                    widget=forms.DateInput(attrs={
                        "type":"date"
                    })

    )
    class Meta:
        model = profile
        fields = '__all__'

