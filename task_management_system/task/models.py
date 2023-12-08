from django.db import models
from category.models import TaskCategory

# Create your models here.


class Task(models.Model):
    taskTitle = models.CharField(max_length=50)
    taskDescription = models.TextField()
    isCompleted = models.BooleanField(default=False)
    taskAssignDate = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(TaskCategory)

    def __str__(self):
        return self.taskTitle
