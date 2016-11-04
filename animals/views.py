from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, render


from animals.models import Animal


def index(request):
    return HttpResponse("Hello World. You're at the animalsAPP index.!")


def details(request, animal_id):

    # animal = get_object_or_404(Animal, pk=animal_id)

    # return render(request=request, template_name="animals/templates/animals/detail.html", context={'animal': animal})

    return HttpResponse(content="You're looking at details {}".format(animal_id))



def results(request, animal_id):
    response = "You're looking at results of animal {}".format(animal_id)
    return HttpResponse(content=response)


def view(request, animal_id):
    return HttpResponse("You're viewing at {}".format(animal_id))

