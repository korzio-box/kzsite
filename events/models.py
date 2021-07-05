from django.db import models
from warehouse.models import Product
from customers.models import Client

# Create your models here.

class Event(models.Model):
    class EStatus(models.TextChoices):
        planned = '1', "Planowane" 
        done = '2', "Zatwierdzone"
    id = models.AutoField(primary_key=True, blank=False, null=False)
    status = models.CharField(max_length=1, choices=EStatus.choices, null=False, blank=False)
    client = models.ForeignKey(Client, null=True, blank=False, on_delete=models.SET_NULL)
    time_add = models.DateTimeField(auto_now=False, auto_now_add=False, blank=False, null=False)
    time_done = models.DateTimeField(auto_now=False, auto_now_add=False, blank=False, null=False)
    Product = models.ManyToManyField(Product, blank=True)


    def __str__(self):
        return str(self.time_done)[0:10] + "/" + str(self.time_done)[11:16] + "/" + str(self.id)


class EventProduct(models.Model):
    id = models.AutoField(primary_key=True, blank=False, null=False)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    event = models.ForeignKey(Event, on_delete=models.SET_NULL, null=True)
    quantity = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        eid = str(self.event)
        return eid + "/" + str(self.id)
