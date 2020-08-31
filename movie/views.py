from django.shortcuts import render

from core.models import Movie

from django.views.generic import ListView, DetailView


class MovieList(ListView):
    model = Movie
    template_name = "movies/movie_list.html"
    paginate_by = 10


class MovieDetail(DetailView):
    model = Movie
    template_name = "movies/movie_detail.html"
