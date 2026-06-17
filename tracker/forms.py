from django import forms
from .models import Device

class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = ['name', 'brand', 'base_market_price', 'condition']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Например, iPhone 15'}),
            'brand': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Например, Apple'}),
            'base_market_price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Рыночная цена в рублях'}),
            'condition': forms.Select(attrs={'class': 'form-select'}),
        }