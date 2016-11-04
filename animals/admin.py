from django.contrib import admin

from .models import Animal
from .models import Person

# Register the following fields to admin backend

admin.site.register(Person)
admin.site.register(Animal)

