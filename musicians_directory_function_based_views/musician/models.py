from django.db import models

# Create your models here.


class Musician(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    instrument_type = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
