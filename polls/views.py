from django.shortcuts import render
from django.http import HttpResponse


def example_view(request):
    return HttpResponse("This is an example view.")


def about(request):
    return HttpResponse('Rango says here is the about page.')
