# from django.conf.urls import url
# from rest_framework.urlpatterns import format_suffix_patterns
# from . import views
#
# ## default api request endpoints
# urlpatterns = [
#     url(r'^snippets/$', views.snippet_list),
#     url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail),
# ]

from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^snippets/$', views.SnippetList.as_view()),
    url(r'^snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view()),
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
]

# register extension patterns
urlpatterns = format_suffix_patterns(urlpatterns)

# at the end of the file append api login portal
urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls')),
]
# after django 1.9+  namespace='rest_framework' is no longer required
