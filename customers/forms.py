from customers.models import Client
from django import forms



class ClientCreateForm(forms.ModelForm):
    first_name = forms.CharField(label='Imię')
    last_name = forms.CharField(label='Nazwisko')
    tel_number = forms.CharField(label='Numer telefonu')
    Hair = forms.ChoiceField(label='Włosy',choices = Client.Choices_Hair)
    class Meta:
        model = Client
        exclude = ('',)

class ClientEditForm(forms.ModelForm):
    first_name = forms.CharField(label='Imię')
    last_name = forms.CharField(label='Nazwisko')
    tel_number = forms.CharField(label='Numer telefonu')
    Hair = forms.ChoiceField(label='Włosy',choices = Client.Choices_Hair)
    class Meta:
        model = Client
        exclude = ('',)