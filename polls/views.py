from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category


def index(request):
    return HttpResponse("Rango says hey there partner!")


def example_view(request):
    return HttpResponse('This is an example view.')


def about(request):
    return HttpResponse('Rango says here is the about page.')
