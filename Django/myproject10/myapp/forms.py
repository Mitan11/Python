from django import forms
from .models import Employee

class EmployeesForm(forms.ModelForm):
    class Meta:
        model = Employee
        # fields = ['name', 'email', 'phone']
        # or
        fields = '__all__'