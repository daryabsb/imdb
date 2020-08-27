from django.db import models

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
    ("A", "ACTION"),
    ("D", "DRAMA"),
    ("C", "COMEDY"),
    ("R", "ROMANCE"),
)

LANGUAGE_CHOICES = (
    ("EN", "ENGLISH"),
    ("AR", "ARABIC"),
    ("KU", "KURDISH"),
    ("GR", "GERMAN"),
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
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=1)
    """models.ForeignKey('Category', on_delete=models.SET_NULL)"""
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=2)
    status = models.CharField(choices=STATUS_CHOICES, max_length=2)
    year = models.DateField()
    views_count = models.IntegerField(default=0)
    # tags =

    # download links

    def __str__(self):
        return f"{self.title} ({self.year})"


# watch links
