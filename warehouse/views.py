from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from warehouse.models import *
from warehouse.forms import *

class ProductListView(ListView):
    model = Product
    context_object_name = 'product_list'
    template_name = 'warehouse/product_list.html'

class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product_detail'
    template_name = 'warehouse/product_detail.html'

class ProductCreateView(CreateView):
    model = Product
    context_object_name = 'product_create'
    form_class = ProductCreateForm
    template_name = 'warehouse/product_create.html'

class ProductEditView(UpdateView):
    model = Product
    context_object_name = 'product_edit'
    form_class = ProductEditForm
    template_name = 'warehouse/product_edit.html'


class serviceListView(ListView):
    model = Service
    context_object_name = 'service_list'