from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=15)
    email = models.EmailField()
    roll = models.IntegerField(primary_key=True)
    department = models.CharField(max_length=15)

    def __str__(self):
        return f'{self.roll} {self.name}'
