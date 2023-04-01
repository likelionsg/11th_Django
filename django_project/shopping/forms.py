
from django import forms
from .models import Shopping

class ShoppingForm(forms.Form):
    name = forms.CharField()
    count = forms.IntegerField()
    price = forms.IntegerField()
    store = forms.CharField()

class ShoppingModelForm(forms.ModelForm):
    class Meta:
        model = Shopping
        fields = '__all__'
        # fields = ['name', 'price']