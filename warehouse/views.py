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

class PTypeListView(ListView):
    model = PType
    context_object_name = 'ptype_list'
    template_name = 'warehouse/ptype_list.html'

class PGroupListView(ListView):
    model = PGroup
    context_object_name = 'pgroup_list'
    template_name = 'warehouse/pgroup_list.html'

class PTypeDetailView(DetailView):
    model = PType
    context_object_name = 'ptype_detail'
    template_name = 'warehouse/ptype_detail.html'

class PGrouptDetailView(DetailView):
    model = PGroup
    context_object_name = 'pgroup_detail'
    template_name = 'warehouse/pgroup_detail.html'

class PTypeCreateView(CreateView):
    model = PType
    context_object_name = 'ptype_create'
    form_class = ProductCreateForm
    template_name = 'warehouse/ptype_create.html'

class PGrouproductCreateView(CreateView):
    model = PGroup
    context_object_name = 'pgroup_create'
    form_class = ProductCreateForm
    template_name = 'warehouse/product_create.html'