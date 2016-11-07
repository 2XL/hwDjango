### QuickStart

1. Create Project
```
# Create the project directory
mkdir tutorial
cd tutorial

# Create a virtualenv to isolate our package dependencies locally
virtualenv env
source env/bin/activate  # On Windows use `env\Scripts\activate`

# Install Django and Django REST framework into the virtualenv
# pip install django
# pip install djangorestframework
pip install -r requirements.txt
```

2. Create App template
```
# Set up a new project with a single application
django-admin.py startproject tutorial .  # Note the trailing '.' character
cd tutorial
django-admin.py startapp quickstart
cd ..
```

3. Sync Database
```
python manage.py migrate
```

4. Create Administrator User
```
python manage.py createsuperuser
```

5. Create ModelObject Serializer
```python 
# tutorial/quickstart/serializers.py
from django.contrib.auth.models import User, Group
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

```

6. Create Views
```python
# touch tutorial/quickstart/view.py
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from tutorial.quickstart.serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
```

7. Routing URL
```python
# touch tutorial/urls.py
from django.conf.urls import url, include
from rest_framework import routers
from tutorial.quickstart import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

```

8. Update Settings registering "quickstart" App
```python
INSTALLED_APPS = (
    ...
    'rest_framework',
)

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAdminUser',),
    'PAGE_SIZE': 10
}
```

9. Test our API
```
# start service 
python manage.py runserver <SERVICE_PORT>

## service consumer request
# cURL
curl \
    -H 'Accept: application/json; indent=4' \ # pretty print response
    -u <ADMIN_USERNAME>:<PASS> \ # admin credentials
    <SERVICE_URL>:<SERVICE_PORT>/<API_ENDPOINT> \ # service endpoint
# httpie
http \ 
    -a <ADMIN_USERNAME>:<PASS>
    <SERVICE_URL>:<SERVICE_PORT>/<API_ENDPOINT>

```


