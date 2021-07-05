from django.contrib import admin
from .models import PType, Product, PGroup


# Register your models here.
admin.site.register(Product)
admin.site.register(PGroup)
admin.site.register(PType)