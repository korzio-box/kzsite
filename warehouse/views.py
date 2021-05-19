from django.shortcuts import render
from django.views.generic import ListView, FormView
from warehouse.models import Product

class ProductListView(ListView):
    model = Product
