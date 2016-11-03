from django.db import models
from django.utils import timezone

class Animal(models.Model):

    animal_name = models.CharField(max_length=200)
    animal_birth = models.DateTimeField('date birth', default=timezone.now) # 1st arg is introspective human readable name

    def __str__(self):
        return "Animal({})".format(self.animal_name)


class Person(models.Model):
    person_name = models.CharField(max_length=200)
    person_pet = models.ForeignKey(Animal, on_delete=models.CASCADE)
    person_email = models.EmailField(max_length=30)
    person_details = models.CharField(max_length=3000)
    person_views = models.IntegerField(default=0)

    def __str__(self):
        return "Person({})".format(self.person_name)


"""


"""
