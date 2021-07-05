from customers.models import Client
from django import forms



class ClientCreateForm(forms.ModelForm):
    first_name = forms.CharField(label='Imię')
    last_name = forms.CharField(label='Nazwisko')
    tel_number = forms.CharField(label='Numer telefonu')
    hair = forms.ChoiceField(label='Włosy',choices = Client.CHOICES_HAIR)
    class Meta:
        model = Client
        exclude = ('',)

class ClientEditForm(forms.ModelForm):
    first_name = forms.CharField(label='Imię')
    last_name = forms.CharField(label='Nazwisko')
    tel_number = forms.CharField(label='Numer telefonu')
    hair = forms.ChoiceField(label='Włosy',choices = Client.CHOICES_HAIR)
    class Meta:
        model = Client
        exclude = ('',)