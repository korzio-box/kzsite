from django.contrib import admin
from .models import Event, EventService, EventProduct

# Register your models here.
admin.site.register(Event)
admin.site.register(EventProduct)
admin.site.register(EventService)