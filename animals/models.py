from django.db import models


class Animal(models.Model):
    animal_name = models.CharField(max_length=200)
    animal_birth = models.DateTimeField('date birth') # 1st arg is introspective human readable name


class Person(models.Model):
    person_name = models.CharField(max_length=200)
    person_pet = models.ForeignKey(Animal, on_delete=models.CASCADE)
    person_email = models.EmailField(max_length=30)
    person_details = models.CharField(max_length=3000)
    person_views = models.IntegerField(default=0)

