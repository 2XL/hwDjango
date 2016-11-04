import datetime

from django.core.urlresolvers import reverse
from django.utils import timezone
from django.test import TestCase
from django.test import Client

from .models import Animal

class AnimalMethodTests(TestCase):

    # test model logic
    def test_some_method_here(self):
        """
        <method_name> should return <whatever>
        :return:
        """

        self.assertIs(True, True) # ... <instance>.<method>(), <whatever>


class AnimalViewTests(TestCase):

    # test views
    def test_index_view(self):
        """
        If ... then ...
        :return:
        """
        response = self.client.get(reverse("animals:index"))