from customers.models import Client
from django import forms

hair_choices =(
    ('1', "długie"),
    ('2', "Pół-długie"),
    ('3', "Krótkie")
)

class ClientCreateForm(forms.ModelForm):
    first_name = forms.CharField(label='Imię')
    last_name = forms.CharField(label='Nazwisko')
    tel_number = forms.CharField(label='Numer telefonu')
    Hair = forms.ChoiceField(label='Włosy', choices = hair_choices)
    class Meta:
        model = Client
        exclude = ('',)

class ClientEditForm(forms.ModelForm):
    class Meta:
        model = Client
        exclude = ('',)