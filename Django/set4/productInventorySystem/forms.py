from django import forms
from .models import Inverntory
from django.contrib.auth.models import User

class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inverntory
        fields = '__all__'

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email' , 'password']
        widgets = {
            'password' : forms.PasswordInput()
        }