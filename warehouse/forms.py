from warehouse.models import PGroup, PType, Product
from django import forms

class ProductCreateForm(forms.ModelForm):
    name = forms.CharField(label='Nazwa')
    barcode = forms.CharField(label='Kod kreskowy')
    group = forms.ModelChoiceField(queryset=PGroup.objects.all(), label='Grupa')
    type = forms.ModelChoiceField(queryset=PType.objects.all(), label='Typ')
    price = forms.DecimalField(label='Cena')
    class Meta:
        model = Product
        exclude = ('',)

class ProductEditForm(forms.ModelForm):
    name = forms.CharField(label='Nazwa')
    barcode = forms.CharField(label='Kod kreskowy')
    group = forms.ModelChoiceField(queryset=PGroup.objects.all(), label='Grupa')
    type = forms.ModelChoiceField(queryset=PType.objects.all(), label='Typ')
    price = forms.DecimalField(label='Cena')
    class Meta:
        model = Product
        exclude = ('',)
    