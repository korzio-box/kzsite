from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from customers.models import *
from customers.forms import *

class ClientListView(ListView):
    model = Client
    context_object_name = 'client_list'
    template_name = 'customers/client_list.html'
    
class ClientCreateView(CreateView):
    model = Client
    context_object_name = 'client_create'
    form_class = ClientCreateForm
    template_name = 'customers/client_create.html'

class ClientDetailView(DetailView):
    model = Client
    context_object_name = 'client_detail'
    template_name = 'customers/client_detail.html'

class ClientEditView(UpdateView):
    model = Client
    context_object_name = 'client_edit'
    form_class = ClientEditForm
    template_name = 'customers/client_edit.html'
