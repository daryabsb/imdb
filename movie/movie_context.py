from core.models import Movie


def slider_movies(request):
    movies = Movie.objects.all().order_by()
    return movies