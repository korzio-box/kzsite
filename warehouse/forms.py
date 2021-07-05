from warehouse.models import PGroup, PType, Product
from django import forms

class ProductCreateForm(forms.ModelForm):
    name = forms.CharField(label='Nazwa')
    barcode = forms.CharField(label='Kod kreskowy')
    pors = forms.ChoiceField(label='Rodzaj',choices = Product.CHOICES_PORS)
    group = forms.ModelChoiceField(queryset=PGroup.objects.all(), label='Grupa')
    type = forms.ModelChoiceField(queryset=PType.objects.all(), label='Typ')
    price = forms.DecimalField(label='Cena')
    class Meta:
        model = Product
        exclude = ('',)

class ProductEditForm(forms.ModelForm):
    name = forms.CharField(label='Nazwa')
    barcode = forms.CharField(label='Kod kreskowy')
    pors = forms.ChoiceField(label='Rodzaj',choices = Product.CHOICES_PORS)
    group = forms.ModelChoiceField(queryset=PGroup.objects.all(), label='Grupa')
    type = forms.ModelChoiceField(queryset=PType.objects.all(), label='Typ')
    price = forms.DecimalField(label='Cena')
    class Meta:
        model = Product
        exclude = ('',)

class PTypeCreateForm(forms.ModelForm):
    name = forms.CharField(label='Nazwa')
    class Meta:
        model = PType
        exclude = ('',)

class PTypeEditForm(forms.ModelForm):
    name = forms.CharField(label='Nazwa')
    class Meta:
        model = PType
        exclude = ('',)

class PGroupCreateForm(forms.ModelForm):
    name = forms.CharField(label='Nazwa')
    class Meta:
        model = PGroup
        exclude = ('',)

class PGroupEditForm(forms.ModelForm):
    name = forms.CharField(label='Nazwa')
    class Meta:
        model = PGroup
        exclude = ('',)


    