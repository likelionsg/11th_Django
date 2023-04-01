
from django import forms
from .models import Shopping

class ShoppingForm(forms.Form):
    name = forms.CharField()
    count = forms.IntegerField()
    price = forms.IntegerField()
    store = forms.CharField()