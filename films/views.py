from django.shortcuts import render
from django.views.generic import ListView
from .models import Film


class HomePage(ListView):
    model = Film
    # template = 'films/main.html'
    # context_object_name = 'home'
