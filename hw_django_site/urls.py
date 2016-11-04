"""hwDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""

from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings

from rest_framework import routers

from hw_django_site import views


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api/',include('api.urls')),
    url(r'^rest/', include('rest_framework.urls', namespace='rest_framework')),
    url(regex=r'^$', view=views.index, name='index'),

    # url(regex=r'^name', view=views.index, name='index'),
    url(r'^admin/', view=include(admin.site.urls)),
    # url(r'^animals/', include('animals.urls', namespace='animals'))
]


# if settings.DEBUG:
#     import debug_toolbar
#     urlpatterns += [
#         # url(r'^__debug__/',include(debug_toolbar.urls)),
#         # the namespace is optional for  Django 1.9+
#     ]
