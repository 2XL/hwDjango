from django.db import models


class Task(models.Model):
    complited = models.BooleanField(default=False)
    title = models.CharField(max_length=100)
    descritpion = models.TextField()
