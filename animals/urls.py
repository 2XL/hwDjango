# from django.conf.urls.defaults import *
from django.conf.urls import url
from django.contrib import admin

from . import views


app_name = "animals"

urlpatterns = [
    # ex: /animals/
    url(r'^$', views.index, name='index'),
    # ex: /animals/5/
    url(r'^(?P<animal_id>[0-9]+)/$', views.details, name='details'),
    # ex: /animals/5/results/
    url(r'^(?P<animal_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /animals/5/view/
    url(r'^(?P<animal_id>[0-9]+)/view/$', views.view, name='view'),
]