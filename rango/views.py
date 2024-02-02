from django.http import HttpResponse
from django.shortcuts import render


def example_view(request):
    return HttpResponse('This is an example view.')


def about(request):
    return render(request, 'rango/about.html')
