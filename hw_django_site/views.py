from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello World. You're at the hw_django_site index.!")

