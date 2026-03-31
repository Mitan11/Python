from django import forms
from .models import Inverntory

class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inverntory
        fields = '__all__'
