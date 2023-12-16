from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from musician.models import Musician

# Create your models here.


class Album(models.Model):
    album_name = models.CharField(max_length=40)
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE)
    release_date = models.DateField()
    RATING_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]

    rating = models.PositiveIntegerField(choices=RATING_CHOICES, default=None)

    def __str__(self):
        return self.album_name
