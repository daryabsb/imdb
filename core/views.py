from django.shortcuts import render

from .models import Movie

from django.views.generic import ListView, DetailView


class Home(ListView):
    model = Movie
    template_name = "home.html"