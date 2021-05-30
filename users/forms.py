from django.forms import ModelForm
from .models import Order,Address,Cart
from django import forms

class CartForm(ModelForm):
    class Meta:
        model = Cart
        fields = ('quantity',)

class RemoveForm(forms.Form):
    order_id = forms.IntegerField()

class SearchForm(forms.Form):
    username = forms.CharField()

