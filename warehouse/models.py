from django.urls import reverse
from django.db import models


class PGroup(models.Model):
    id = models.AutoField(primary_key=True, blank=False, null=False)
    name = models.CharField(max_length=50, null=False, blank=False, unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name = self.name.capitalize()
        super(PGroup, self).save(*args, **kwargs)


class SGroup(models.Model):
    id = models.AutoField(primary_key=True, blank=False, null=False)
    name = models.CharField(max_length=50, null=False, blank=False, unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name = self.name.capitalize()
        super(SGroup, self).save(*args, **kwargs)

class PType(models.Model):
    id = models.AutoField(primary_key=True, blank=False, null=False)
    name = models.CharField(max_length=50, null=False, blank=False, unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name = self.name.capitalize()
        super(PType, self).save(*args, **kwargs)

class Product(models.Model):
    id = models.AutoField(primary_key=True, blank=False, null=False)
    name = models.CharField(max_length=50, null=False, blank=False, unique=True)
    barcode = models.CharField(max_length=50, null=False, blank=False, unique=True)
    group = models.ForeignKey(PGroup, null=True, blank=False, on_delete=models.SET_NULL)
    type = models.ForeignKey(PType, null=True, blank=False, on_delete=models.SET_NULL)
    price = models.DecimalField(null=True, blank=True, unique=False, decimal_places=2, max_digits=5)




    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name = self.name.capitalize()
        super(Product, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('product_detail', args=[str(self.id)])

class Service(models.Model):
    id = models.AutoField(primary_key=True, blank=False, null=False)
    name = models.CharField(max_length=50, null=False, blank=False, unique=True)
    group = models.ForeignKey(SGroup, null=True, blank=False, on_delete=models.SET_NULL)
    price = models.DecimalField(null=True, blank=True, unique=False, decimal_places=2, max_digits=5)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name = self.name.capitalize()
        super(Service, self).save(*args, **kwargs)