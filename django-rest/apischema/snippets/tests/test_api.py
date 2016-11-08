from rest_framework.test import APIRequestFactory
import json
# Using the standard RequestFactory API to create a form POST request

#################
# API - FACTORY
#################
factory = APIRequestFactory() # methods available
"""
factory
    .get
    .post
    .put
    .path
    .delete
    .head
    .options
"""
# sample request
request = factory.post('/notes/',{'title': 'note title here'}, format='json')
"""
format=     # default {multipart}
    multipart
    json
"""
# sample request, encoded body
request = factory.post('/notes/', json.dumps({'title': 'descriptive title here'}), content_type='application/json')
"""
difference between:
    RequestFactory && : need explicitly encode the data
    APIRequestFactory : multipart data will be encoded for methods
"""
# Forcing authentication
from rest_framework.test import force_authenticate
from django.contrib.auth.models import User

factory = APIRequestFactory()
user = User.objects.get(username='olivia')


# factory = APIRequestFactory()
# user = User.objects.get(username='olivia')
# view = AccountDetail.as_view()
#
# # Make an authenticated request to the view...
# request = factory.get('/accounts/django-superstars/') # this generates HttpRequest
# force_authenticate(request, user=user, token=user.token)
# response = view(request)  # this generates Request

# The CSRF validation takes place inside the view, so the request factory needs to disable view-level cSRF checks
factory = APIRequestFactory(enforce_csrf_checks=True)




################
# API - Client #
################

from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token

#
client = APIClient()
client.post('/notes/', {'title': 'new idea'}, format='json')


# Authenticating, perform request against any SessionAuthentication Views
client.login(username='user', password='secret')

# auth with token
token = Token.objects.get(user__username='user')

# include an appropriate `Authorization` header on all requests
client.credentials(HTTP_AUTHORIZATION='Token '+token.key)


# stop including any credentials
# calling credentials twice, un sets the previous existing credentials
# stop
client.logout()

# enforcing CSRF validation
client = APIClient(enforce_csrf_checks=True)
# require client login to validate CSRF views and grant access
# client.logout()


# Request clients

from rest_framework.test import RequestsClient
client = RequestsClient()

# requirement fully qualified URLs
response = client.get('http://testserver/users')
assert response.status_code == 200


# Headers & Authentication

from requests.auth import HTTPBasicAuth

client.auth = HTTPBasicAuth('user', 'pass')
client.headers.update({'x-test': 'true'})


# CSRF, when using SessionAuthentication we need to include a CSRF token to any requests

client = RequestsClient()

# Obtain a CSRF token
response = client.get('/homepage/') # 1st request , retrieve a token
assert response.status_code == 200
csrftoken = response.cookies['csrftoken'] # store the token for upcoming requests

# Interact with the API
response = client.post('/organisations/', json={
    'name': 'MegaCorp',
    'status': 'active'
}, headers={'X-CSRFToken': csrftoken})
assert response.status_code == 200


## core api client

from coreapi import Client as CoreAPIClient

client = CoreAPIClient()
# fetch api schema
schema = client.get('http://testserver/schema/')

# create a new schema instance
params = {'name': 'Obytes', 'status': 'active'}
client.action(schema, ['organisations', 'create'], params)

# ensure that the organisation exists in the listing
data = client.action(schema, ['organionts', 'list'])
assert (len(data) == 1)
assert (data == [{'name': 'Obtes', 'status': 'active'}])

# Headers & Authentication

from requests.auth import HTTPBasicAuth

client = CoreAPIClient()
client.session.auth = HTTPBasicAuth('user', 'pass')
client.session.headers.update({'x-test':'true'})






