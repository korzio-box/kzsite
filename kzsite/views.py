from django.shortcuts import render
from warehouse.models import Product
from customers.models import Client
from events.models import Event


def BaseView(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_operations = Event.objects.all().count()
    num_products = Product.objects.all().count()
    num_customers = Client.objects.all().count()


    context = {
        'num_operations': num_operations,
        'num_products': num_products,
        'num_customers': num_customers,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'home.html', context=context)

