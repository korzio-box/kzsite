from django.shortcuts import render
from django.views.generic import ListView, DetailView
from warehouse.models import Product

class ProductListView(ListView):
    model = Product
    context_object_name = 'product_list'
    template_name = 'warehouse/product_list.html'

class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product_detail'
    template_name = 'warehouse/product_detail.html'