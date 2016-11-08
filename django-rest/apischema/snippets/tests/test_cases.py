from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from animals.models import Person
from animals.models import UserDetail
from django.contrib.auth.models import User
from rest_framework.test import APIRequestFactory
import json


class AccountTests(APITestCase):

    def test_create_account(self):
        """
        Ensure we can create a new account object.
        """
        url = reverse('account-list')
        data = {'name': 'DabApps'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Person.objects.count(), 1)
        self.assertEqual(Person.objects.get().name, 'DabApps')

        # inspect response data [BETTER] / skip parsing stage
    def test_get_client(self):
        response = self.client.get('/users/4/')
        self.assertEqual(response.data, {'id': 4, 'username': 'lauren'})

        # inspect response.content [OKEY]
    def test_set_name(self):
        response = self.client.get()
        self.assertEqual(json.load(response.content), {'id': 4, 'username': 'lauren'})

    def test_render_response(self):
        factory = APIRequestFactory()
        view = UserDetail.as_view() # load django APIView
        request = factory.get('/users/4') # get api view data
        response = view(request, pk='4') # fill APIView with data to obtain APIView Iinstance
        response.render()  # compile result, to obtain specific view

        # cannot access response.content without compile
        # [content attribute belongs to the request fields of the response]
        self.assertEqual(response.content, '{"username": "lauren", "id": 4}')
