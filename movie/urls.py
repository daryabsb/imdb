from django.urls import path
from .views import (
                MovieList, 
                MovieDetail, 
                MovieCategory, 
                MovieLanguage, 
                MovieSearch
                )

app_name = "movie"
urlpatterns = [
    path("", MovieList.as_view(), name="movie-list"),
    path("category/<str:category>", MovieCategory.as_view(), name="movie-category"),
    path("language/<str:lang>", MovieLanguage.as_view(), name="movie-language"),
    path("search/", MovieSearch.as_view(), name="movie-search"),
    path("<int:pk>", MovieDetail.as_view(), name="movie-detail"),
]