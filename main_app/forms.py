from django import forms
from .models import *

class Contactform(forms.ModelForm):
    class Meta:
        model = ContactInfo
        fields = '__all__'