from django.shortcuts import render

from core.models import Movie, MovieLink

from django.views.generic import ListView, DetailView


class MovieList(ListView):
    model = Movie
    template_name = "movies/movie_list.html"
    paginate_by = 10


class MovieDetail(DetailView):
    model = Movie
    template_name = "movies/movie_detail.html"

    def get_object(self):
        object = super(MovieDetail, self).get_object()
        object.views_count += 1
        object.save()
        return object

    def get_context_data(self, **kwargs):
        context = super(MovieDetail, self).get_context_data(**kwargs)
        context["links"] = MovieLink.objects.filter(movie=self.get_object())
        return context


class MovieCategory(ListView):
    model = Movie

    def get_queryset(self):
        category_id = self.kwargs["pk"]  # "get_object_or_404()"
        movies = Movie.objects.filter(category=category_id)

    def get_context_data(self):
        context = super(MovieCategory, self).get_context_data(**kwargs)
        context["movie_category"] = self.category_id
        return context
