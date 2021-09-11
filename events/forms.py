from django.db.models.expressions import Value
from django.forms.models import inlineformset_factory
from django.forms.widgets import HiddenInput
from events.models import Event, EventProduct
from django import forms
from warehouse.models import Product
from customers.models import Client

class DateInput(forms.DateInput):
    input_type = 'date'

class EventFormIn(forms.ModelForm):
    status = forms.ChoiceField(label='Status',choices = Event.CHOICES_STATUS, initial=2)
    client = forms.ModelChoiceField(queryset=Client.objects.all(), label='Klient', widget=HiddenInput, required = False)
    outcome = forms.BooleanField(initial=False, widget=HiddenInput, required = False)

    class Meta:
        model = Event
        exclude = ('',)

class EventForm(forms.ModelForm):
    status = forms.ChoiceField(label='Status',choices = Event.CHOICES_STATUS)
    client = forms.ModelChoiceField(queryset=Client.objects.all(), label='Klient')
    outcome = forms.BooleanField(initial=True, widget=HiddenInput)
    time_done = forms.DateTimeField(widget=forms.DateTimeInput(attrs= {'type':'datetime-local'}),label='Termin')

    class Meta:
        model = Event
        exclude = ('',)
        
EventProductFormset = inlineformset_factory(Event, EventProduct,
                                            fields=('product', 'quantity'),
                                            extra=8)
                                            ##form=EventForm)
