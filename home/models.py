from django.db import models


class Task(models.Model):
    tasktitle = models.CharField(max_length=255)
    taskdescription = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return self.tasktitle

# Create your models here.
