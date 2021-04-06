from django.db import models


class Band(models.Model):
    GENRE_CHOICES = (
        (-1, 'not defined'),
        (0, 'rock'),
        (1, 'metal'),
        (2, 'pop'),
        (3, 'hip hop'),
        (4, 'electronic')
    )

    name = models.CharField(max_length=64)
    year = models.IntegerField(null=True)
    still_activate = models.BooleanField(default=True)
    genre = models.IntegerField(choices=GENRE_CHOICES, default=-1)


class Category(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(null=True)

class Articles(models.Model):
    STATUS_CHOICES = (
        ('inprogress', 'w trakcie pisania'),
        ('waiting', 'czeka na akceptację'),
        ('published', 'opublikowany'),
    )
    title = models.CharField(max_length=120)
    author = models.CharField(max_length=64, null=True)
    content = models.TextField()
    date_added = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)

class Album(models.Model):

    RATING_CHOICES = (
        (0, 'awful'),
        (1, 'weak'),
        (2, 'so so'),
        (3, 'good'),
        (4, 'very good'),
        (5, 'excelLent'),
    )

    title = models.CharField(max_length=256)
    year = models.PositiveIntegerField()
    rating = models.PositiveSmallIntegerField(choices=RATING_CHOICES)
    band = models.ForeignKey(Band, on_delete=models.CASCADE, null=True)




