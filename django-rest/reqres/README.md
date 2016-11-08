## Requests and Response

* Request objects

```
# class HttpRequest
request.POST  # Only handles form data.  Only works for 'POST' method.
request.data  # Handles arbitrary data.  Works for 'POST', 'PUT' and 'PATCH' methods.
```

* Response objects

```
# class TemplateResponse # uses content negotiation to determine the correct content type to return to the client
return Reponse(data)
```

* Status codes

```
# Explicit identifiers for each status code...
status.HTTP_400_BAD_REQUEST
``` 

* Wrapping API views
    1. @api_view : decorator for working with function based views
    2. APIView : class for working with class-based views.

```
```

* Pulling it all together

```
# views.py
```

* Adding optional format Suffixes to our API URLs


```
<SERVICE_HOST>/<API>/<ENDPOINT>/<PK>.<EXTENSION>
http://example.com/api/items/4.json


# request with either "Accept" header, "Content-Type" header or Appending a format suffix
http http://127.0.0.1:8000/snippets.json  # JSON suffix
http http://127.0.0.1:8000/snippets.api   # Browsable API suffix
# POST using form data
http --form POST http://127.0.0.1:8000/snippets/ code="print 123"
# POST using JSON
http --json POST http://127.0.0.1:8000/snippets/ code="print 456"


```