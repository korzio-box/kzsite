from django.contrib import admin
from .models import Product, Service, PGroup, SGroup


# Register your models here.
admin.site.register(Product)
admin.site.register(Service)
admin.site.register(PGroup)
admin.site.register(SGroup)