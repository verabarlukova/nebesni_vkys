from django import forms
from .models import Client

class OrderForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'phone', 'address'] # Пользователь заполнит эти поля