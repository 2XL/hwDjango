# Serialization

The first thing we need to get started on our Web API is to provide a way
of serializing and deserializing the snippet instances into representations
such as JSON.


## Serializers: Serialize/Deserialize

```
################################
## Object to JSON (serializer)
################################
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

snippet = Snippet(code='foo = "bar"\n')
snippet.save()

snippet = Snippet(code='print "hello, world"\n')
snippet.save()
serializer = SnippetSerializer(snippet)

serializer.data
# {'id': 2, 'title': u'', 'code': u'print "hello, world"\n', 
#   'linenos': False, 'language': u'python', 'style': u'friendly'}

################################
## JSON to Object (deserializer)
################################
from django.utils.six import BytesIO

# 1. we parse a stream into Python native datatypes...
stream = BytesIO(content)
data = JSONParser().parse(stream)

# 2. restore those native datatypes into a fully populated object instance
serializer = SnippetSerializer(data=data)
serializer.is_valid()
# True
serializer.validated_data
# OrderedDict([('title', ''), ('code', 'print "hello, world"\n'), ('linenos', False), ('language', 'python'), ('style', 'friendly')])
serializer.save()
# <Snippet: Snippet object>

```

## ModelSerializers: Do Not Reinvent the Wheel (automate)

### Update Serializer class with ModelSerializer
```python 
# replace the serializer class:
class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style')
```
### Inspect Serializer
```python
from snippets.serializers import SnippetSerializer
serializer = SnippetSerializer()
print(repr(serializer))
# SnippetSerializer():
#    id = IntegerField(label='ID', read_only=True)
#    title = CharField(allow_blank=True, max_length=100, required=False)
#    code = CharField(style={'base_template': 'textarea.html'})
#    linenos = BooleanField(required=False)
#    language = ChoiceField(choices=[('Clipper', 'FoxPro'), ('Cucumber', 'Gherkin'), ('RobotFramework', 'RobotFramework'), ('abap', 'ABAP'), ('ada', 'Ada')...
#    style = ChoiceField(choices=[('autumn', 'autumn'), ('borland', 'borland'), ('bw', 'bw'), ('colorful', 'colorful')...
```

## Django Views powered with Serializer (Controller Logic)


```
<app_name>/views.py
def <app_name>_detail(request, pk)
# LIST || CREATE
def <app_name_list(request, pk)
# GET | UPDATE | DELETE
```


A mixin is a special kind of multiple inheritance, use case:
 1. You want to provide a lot of optional features for a class
 2. You want to use particular feature in a lot of different classes

 * I can make a plain old request object by saying:
```python
from werkzeug import BaseRequest

class Request(BaseRequest):
    pass
```
 * If I want to add accept header support, I would make that
```python
from werkzeug import BaseRequest, AcceptMixin

class Request(BaseRequest, AcceptMixin):
    pass
```

 * If I wanted to make a request object that supports accept headers, etags, authentication, and user agent support, I could do this:
```python
from werkzeug import BaseRequest, AcceptMixin, ETagRequestMixin, UserAgentMixin, AuthorizationMixin

class Request(BaseRequest, AcceptMixin, ETagRequestMixin, UserAgentMixin, AuthorizationMixin):
    pass
```

## Authentication & Permissions

Features:



## Testing the API

# list
http http://127.0.0.1:8888/snippets/

# get
http http://127.0.0.1:8888/snippets/1/