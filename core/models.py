from django.db import models
from django.utils.text import slugify

"""
We will use CATEGORY_CHOICES for the sake of this tutorial
But normally, we will make a model to make the choices dynamic
and it's done as below:

class Category(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000, blank=True, null=True)
    image = models.ImageField(upload_to='movies') 

Then we will reference it as an FK in the Movie model

"""


CATEGORY_CHOICES = (
    ("action", "ACTION"),
    ("drama", "DRAMA"),
    ("comedy", "COMEDY"),
    ("romance", "ROMANCE"),
)

LANGUAGE_CHOICES = (
    ("english", "ENGLISH"),
    ("arabic", "ARABIC"),
    ("kurdish", "KURDISH"),
    ("germany", "GERMAN"),
)

STATUS_CHOICES = (
    ("RA", "RECENTLY ADDED"),
    ("MW", "MOST WATCHED"),
    ("TR", "TOP RATED"),
)


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000, blank=True, null=True)
    image = models.ImageField(upload_to="movies")
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=15)
    """models.ForeignKey('Category', on_delete=models.SET_NULL)"""
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=15)
    status = models.CharField(choices=STATUS_CHOICES, max_length=2)
    cast = models.CharField(max_length=100, blank=True, null=True)
    year = models.DateField()
    views_count = models.IntegerField(default=0)
    slug = models.SlugField(blank=True, null=True)
    movie_trailer = models.URLField(default='#')
    # tags =

    # download links

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Movie, self).save( *args, **kwargs)

    def __str__(self):
        return f"{self.title} ({self.year})"


# watch links

LINK_Choices = (
    ("D", "Download Link"),
    ("W", "Watch Link"),
)


class MovieLink(models.Model):
    movie = models.ForeignKey(
        "Movie", related_name="movie_download_links", on_delete=models.CASCADE
    )
    type = models.CharField(choices=LINK_Choices, max_length=1)
    link = models.URLField()

    def __str__(self):
        return f"{self.movie.title} ({self.type})'s link"
