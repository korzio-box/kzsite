from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView, FormView
from events.models import *
from events.forms import *
from django.http import HttpResponseRedirect
from django.views.generic.detail import SingleObjectMixin
from django.db import transaction



class EventListView(ListView):
    model = Event
    context_object_name = 'event_list'
    template_name = 'events/event_list.html'
    
class EventCreateView(CreateView):
    ##model = Event
    context_object_name = 'event_create'
    form_class = EventForm
    template_name = 'events/event_create.html'
    success_url=reverse_lazy('event_list')

    def get_context_data(self, **kwargs):
        context = super(EventCreateView, self).get_context_data(**kwargs)
        if self.request.POST:
            context['event_formset'] = EventProductFormset(self.request.POST, instance=self.object)
        else:
            context['event_formset'] = EventProductFormset()
        return context

    def form_valid(self, form):
        context = self.get_context_data(form=form)
        formset = context['event_formset']
        if formset.is_valid():
            response = super().form_valid(form)
            formset.instance = self.object
            formset.save()
            return response
        else:
            return super(EventCreateView, self).form_invalid(form)


class EventDetailView(DetailView):
    model = Event
    context_object_name = 'event_detail'
    template_name = 'events/event_detail.html'

class EventEditView(UpdateView):
    model = Event
    context_object_name = 'event_edit'
    form_class = EventForm
    template_name = 'events/event_edit.html'
