from django.shortcuts import render
from django.views.generic import ListView
# Create your views here.
from .models import*

class HomePageView(ListView):
    model = List
    template_name = 'index.html'
    context_object_name = 'list_types'