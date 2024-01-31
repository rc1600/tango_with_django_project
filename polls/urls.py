from django.urls import path
from . import views
from .views import about

app_name = 'polls'

urlpatterns = [
    path('example/', views.example_view, name='example'),
    path('about/', about, name='about'),
]
