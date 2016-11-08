"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".
Replace this with more appropriate tests for your application.
"""
from django.test import TestCase

from animals.models import User
from animals.views import UserDetail
from django.db import models

class AnimalModelTest(TestCase):
    def test_saving_and_retrieving_items(self):
        first_item = User()
        first_item.text = 'The first (ever) list item'
        first_item.save()
        second_item = User()
        second_item.text = 'Item the second'
        second_item.save()
        saved_items = User.objects.all()
        self.assertEqual(saved_items.count(), 2)
        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'The first (ever) list item')
        self.assertEqual(second_saved_item.text, 'Item the second')



# to run the test
# python manage.py test # all test_xxx are run
# python manage.py test <appname>.<TestCaseClass> # only the this tset

# or run with django-nose (deprecated after django 1.6+)
# python manage.py test <appname>.test:<TestCaseClass>.<TestMethod>