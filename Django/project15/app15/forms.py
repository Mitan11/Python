from django import forms
from .models import student
from django.contrib.auth.models import User
class studentForm(forms.ModelForm):
    class Meta:
        model=student
        fields='__all__'

        
class loginForm(forms.Form):
    username=forms.CharField(max_length=40)
    password=forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','email','password']
        widgets={
            'password':forms.PasswordInput()
        }