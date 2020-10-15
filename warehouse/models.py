from django.db import models

class PGroup(models.Model):
    id = models.AutoField(primary_key=True, blank=False, null=False)
    group_name = models.CharField(max_length=50, null=False, blank=False, unique=True)

    def __str__(self):
        return self.group_name

    def save(self, *args, **kwargs):
        self.group_name = self.group_name.capitalize()
        super(PGroup, self).save(*args, **kwargs)


class SGroup(models.Model):
    id = models.AutoField(primary_key=True, blank=False, null=False)
    group_name = models.CharField(max_length=50, null=False, blank=False, unique=True)

    def __str__(self):
        return self.group_name

    def save(self, *args, **kwargs):
        self.group_name = self.group_name.capitalize()
        super(SGroup, self).save(*args, **kwargs)


class Product(models.Model):
    id = models.AutoField(primary_key=True, blank=False, null=False)
    product_name = models.CharField(max_length=50, null=False, blank=False, unique=True)
    product_barcode = models.CharField(max_length=50, null=False, blank=False, unique=True)
    product_group = models.ForeignKey(PGroup, null=True, blank=False, on_delete=models.SET_NULL)
    product_price = models.DecimalField(null=True, blank=True, unique=False, decimal_places=2, max_digits=5)

    class Ptype(models.TextChoices):
        paint = '1', "Farba"
        care = '2', "Pielęgnacja"
        sell = '3', "Sprzedaż"

    Ptype = models.CharField(max_length=1, choices=Ptype.choices, blank=False)

    def __str__(self):
        return self.product_name

    def save(self, *args, **kwargs):
        self.product_name = self.product_name.capitalize()
        super(Product, self).save(*args, **kwargs)


class Service(models.Model):
    id = models.AutoField(primary_key=True, blank=False, null=False)
    service_name = models.CharField(max_length=50, null=False, blank=False, unique=True)
    service_group = models.ForeignKey(SGroup, null=True, blank=False, on_delete=models.SET_NULL)
    service_price = models.DecimalField(null=True, blank=True, unique=False, decimal_places=2, max_digits=5)

    def __str__(self):
        return self.service_name

    def save(self, *args, **kwargs):
        self.service_name = self.service_name.capitalize()
        super(Service, self).save(*args, **kwargs)