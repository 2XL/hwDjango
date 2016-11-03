import datetime

from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Animal(models.Model):

    animal_name = models.CharField(max_length=200)
    animal_birth = models.DateTimeField('date birth', default=timezone.now) # 1st arg is introspective human readable name

    def was_born_last_year(self):
        return self.animal_birth >= timezone.now() - datetime.timedelta(weeks=54)

    def __str__(self):
        return "Animal({})".format(self.animal_name)

@python_2_unicode_compatible
class Person(models.Model):
    person_name = models.CharField(max_length=200)
    person_pet = models.ForeignKey(Animal, on_delete=models.CASCADE)
    person_email = models.EmailField(max_length=30)
    person_details = models.CharField(max_length=3000)
    person_views = models.IntegerField(default=0)

    def __str__(self):
        return "Person({})".format(self.person_name)


"""

@python_2_unicode_compatible => to support python 2

def __str__(self): # important to implement this method


"""
