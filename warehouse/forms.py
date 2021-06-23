from warehouse.models import Product
from django import forms

class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ('',)

class ProductEditForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ('',)
    