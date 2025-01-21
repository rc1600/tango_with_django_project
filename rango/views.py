from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # Ensure the anchor tag is rendered as a hyperlink
    return HttpResponse("Rango says hey there partner! <a href='/rango/about/'>About</a>")

def about(request):
    # Add a link back to the index page
    return HttpResponse("Rango says here is the about page. <a href='/rango/'>Back to the index page</a>")

