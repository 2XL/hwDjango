from django.contrib import admin

from .models import Animal
from .models import Person


# Register the following fields to admin backend


class AnimalAdmin(admin.ModelAdmin):
    fields = ['animal_name']


class PersonAdmin(admin.ModelAdmin):
    fieldsets = [
        ('SET 1 NAME', {'fields': ['person_name']})
        ('SET 2 NAME', {'fields': ['person_email']})
    ]
    # fields = ['person_name']


# admin.site.register(Person)
# admin.site.register(Animal)

admin.site.register(Animal, AnimalAdmin)
admin.site.register(Person, PersonAdmin)
