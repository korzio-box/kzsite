from django.forms.models import inlineformset_factory
from events.models import Event, EventProduct
from django import forms
from warehouse.models import Product
from customers.models import Client


class EventForm(forms.ModelForm):
    status = forms.ChoiceField(label='Status',choices = Event.CHOICES_STATUS)
    client = forms.ModelChoiceField(queryset=Client.objects.all(), label='Klient')   

    class Meta:
        model = Event
        exclude = ('',)
        
EventProductFormset = inlineformset_factory(Event, EventProduct,
                                            fields=('product', 'quantity'),)
                                            ##form=EventForm)
