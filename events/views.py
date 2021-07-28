from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from events.models import *
from events.forms import *


class EventListView(ListView):
    model = Event
    context_object_name = 'event_list'
    template_name = 'events/event_list.html'
    
class EventCreateView(CreateView):
    model = Event
    context_object_name = 'event_create'
    form_class = EventCreateForm
    template_name = 'events/event_create.html'

class EventDetailView(DetailView):
    model = Event
    context_object_name = 'event_detail'
    template_name = 'events/event_detail.html'

class EventEditView(UpdateView):
    model = Event
    context_object_name = 'event_edit'
    #form_class = EventEditForm
    template_name = 'events/event_edit.html'
