from django.db import models
from django.forms.widgets import HiddenInput, Widget
from warehouse.models import Product
from customers.models import Client
from django.urls import reverse

# Create your models here.

class Event(models.Model):
    id = models.AutoField(primary_key=True, blank=False, null=False)
    client = models.ForeignKey(Client, null=True, blank=True, on_delete=models.SET_NULL)
    time_add = models.DateTimeField(auto_now=True, blank=False, null=False,)
    time_done = models.DateTimeField(auto_now_add=False, blank=False, null=False,)
    outcome = models.BooleanField(blank=True, null=False)
    CHOICES_STATUS = (
        (1, "Planowane"),
        (2, "Wykonane"))

    status = models.PositiveSmallIntegerField(choices=CHOICES_STATUS, blank=True)

    def __str__(self):
        return str(self.time_done)[0:10] + "/" + str(self.time_done)[11:16] + "/" + str(self.id)
    
    def get_absolute_url(self):
        return reverse('event_detail', args=[str(self.id)])



class EventProduct(models.Model):
    id = models.AutoField(primary_key=True, blank=False, null=False)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, verbose_name="Produkt")
    event = models.ForeignKey(Event, on_delete=models.SET_NULL, null=True)
    quantity = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Ilość")

    def __str__(self):
        eid = str(self.event)
        return eid + "/" + str(self.id)
