from django.db.models.aggregates import Aggregate
from django.db.models.expressions import Window
from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView, FormView
from events.models import *
from events.forms import *
from django.http import HttpResponseRedirect
from django.views.generic.detail import SingleObjectMixin
from django.db.models import QuerySet



class EventInCreateView(CreateView):
    model = Event
    context_object_name = 'event_in_create'
    form_class = EventFormIn
    template_name = 'events/event_in_create.html'

    def get_context_data(self, **kwargs):
        context = super(EventInCreateView, self).get_context_data(**kwargs)
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
            return super(EventInCreateView, self).form_invalid(form)

    def get_success_url(self):
        return reverse('product_list')

class EventListView(ListView):
    model = Event
    context_object_name = 'event_list'
    template_name = 'events/event_list.html'
    
class EventCreateView(CreateView):
    model = Event
    context_object_name = 'event_create'
    form_class = EventForm
    template_name = 'events/event_create.html'

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

    def get_success_url(self):
        return reverse('event_list')

class EventDetailView(DetailView):
    model = Event
    context_object_name = 'event_detail'
    template_name = 'events/event_detail.html'
    

class EventEditView(UpdateView):
    model = Event
    context_object_name = 'event_edit'
    form_class = EventForm
    template_name = 'events/event_edit.html'

    def get_context_data(self, **kwargs):
        context = super(EventEditView, self).get_context_data(**kwargs)
        if self.request.POST:
            context['event_formset'] = EventProductFormset(self.request.POST, instance=self.object)
            context['event_formset'].full_clean()
        else:
            context['event_formset'] = EventProductFormset(instance=self.object)
        return context

    def form_valid(self, form):
        context = self.get_context_data(form=form)
        formset = context['event_formset']
        for form in formset.forms:
            if formset.is_valid():
                response = super().form_valid(form)
                formset.instance = self.object
                formset.save()
                return response
            else:
                return super().form_invalid(form)

    def get_success_url(self):
        return reverse('event_list')

class EventInEditView(UpdateView):
    model = Event
    context_object_name = 'event_in_edit'
    form_class = EventFormIn
    template_name = 'events/event_in_edit.html'

    def get_context_data(self, **kwargs):
        context = super(EventInEditView, self).get_context_data(**kwargs)
        if self.request.POST:
            context['event_formset'] = EventProductFormset(self.request.POST, instance=self.object)
            context['event_formset'].full_clean()
        else:
            context['event_formset'] = EventProductFormset(instance=self.object)
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
            return super().form_invalid(form)

    def get_success_url(self):
        return reverse('event_list')