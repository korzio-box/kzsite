from events.models import Event, EventProduct
from django import forms
from warehouse.models import Product
from customers.models import Client


class EventCreateForm(forms.ModelForm):
    status = forms.ChoiceField(label='Status',choices = Event.CHOICES_STATUS)
    time_add = forms.DateTimeField(label='Czas dodania')
    time_done = forms.DateTimeField(label='Czas zakończenia')
    client = forms.ModelChoiceField(queryset=Client.objects.all(), label='Klient')

    class EventProductCreateForm(forms.ModelForm):
        product = forms.ModelMultipleChoiceField(queryset=Product.objects.all(), label='Produkt')
        quantity = forms.DecimalField(label='Ilość')

        class Meta:
            model = EventProduct
            exclude = ('',)

    class Meta:
        model = Event
        exclude = ('',)
