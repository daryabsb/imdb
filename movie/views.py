from django.shortcuts import render

from core.models import Movie, MovieLink

from django.views.generic import ListView, DetailView
from django.views.generic.dates import YearArchiveView


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
    template_name = "movies/movie_list.html"
    paginate_by = 5

    def get_queryset(self):
        self.category = self.kwargs["category"]  # "get_object_or_404()"
        # movies =
        return Movie.objects.filter(category=self.category)

    def get_context_data(self, **kwargs):
        context = super(MovieCategory, self).get_context_data(**kwargs)
        context["movie_category"] = self.category
        return context


class MovieLanguage(ListView):
    model = Movie
    template_name = "movies/movie_list.html"
    paginate_by = 5

    def get_queryset(self):
        self.language = self.kwargs["lang"]  # "get_object_or_404()"
        # movies =
        return Movie.objects.filter(language=self.language)

    def get_context_data(self, **kwargs):
        context = super(MovieLanguage, self).get_context_data(**kwargs)
        context["movie_language"] = self.language
        return context


class MovieSearch(ListView):
    model = Movie
    template_name = "movies/movie_list.html"
    paginate_by = 5

    def get_queryset(self):
        query = self.request.GET.get("query")
        if query:
            object_list = self.model.objects.filter(title__icontains=query)
            # print('Reached')
            # print(query)
            # print(object_list)
        else:
            object_list = self.model.objects.none()
            print("Rejected")
        return object_list


class MovieYear(YearArchiveView):
    queryset = Movie.objects.all()
    template_name = "movies/movie_archive_year.html"
    date_field = "year"
    make_object_list = True
    allow_future = True

    print(queryset)
