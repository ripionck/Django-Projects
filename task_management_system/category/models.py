from django.db import models

# Create your models here.


class TaskCategory(models.Model):
    category = models.CharField(max_length=20)

    def __str__(self):
        return self.category
