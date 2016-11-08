from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, render


from .serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework import generics


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


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

