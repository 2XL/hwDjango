from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

## default api request endpoints
urlpatterns = [
    url(r'^snippets/$', views.snippet_list),
    url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail),
]

# register extension patterns
urlpatterns = format_suffix_patterns(urlpatterns)