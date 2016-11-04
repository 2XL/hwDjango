import datetime

from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Animal(models.Model):

    animal_name = models.CharField(max_length=200)
    animal_birth = models.DateTimeField(verbose_name='date birth', default=timezone.now) # 1st arg is introspective human readable name
    # the default verbose name is the attribute name
    def was_born_last_year(self):
        return self.animal_birth >= timezone.now() - datetime.timedelta(weeks=54)

    def __str__(self):
        return "Animal({})".format(self.animal_name)


@python_2_unicode_compatible
class Person(models.Model):
    GENDER = (('M', 'Male'), ('F', 'Female'))
    # person_id = models.AutoField(primary_key=True)
    person_name = models.CharField(max_length=200)
    person_pet = models.ForeignKey(Animal, on_delete=models.CASCADE)
    person_email = models.EmailField(max_length=30)
    person_details = models.CharField(max_length=3000)
    person_views = models.IntegerField(default=0)
    person_gender = models.CharField(max_length=1, default='M', choices=GENDER)

    def __str__(self):
        return "Person({})".format(self.person_name)

    # overriding
    def save(self, *args, **kwargs):
        super(Person, self).save(*args,**kwargs) # call the original method
        pass

    #
    # def delete(self, using=None):
    #     pass


class CommonInfo(models.Model):
    info = models.CharField(max_length=10)

    class Meta:
        abstract = True


class MaleHuman(CommonInfo):
    home_land = models.CharField(max_length=5)
    class Meta(CommonInfo.Meta):
        db_table = 'male_info'


class FemaleHuman(CommonInfo):
    is_pregnant = models.CharField(max_length=5)


"""

@python_2_unicode_compatible => to support python 2

def __str__(self): # important to implement this method


"""
