from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def korzio_response(request):
    return HttpResponse("test korzio")