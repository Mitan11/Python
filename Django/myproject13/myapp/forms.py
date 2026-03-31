from django import forms
from django.contrib.auth.models import User
from .models import Employee

class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }

class EmpForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'