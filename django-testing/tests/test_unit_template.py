"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".
Replace this with more appropriate tests for your application.
"""
from django.test import TestCase


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that x+y = x+y
        :return:
        """
        self.assertEqual(1+1, 1+1)


# to run the test
# python manage.py test # all test_xxx are run
# python manage.py test <appname>.<TestCaseClass> # only the this tset

# or run with django-nose (deprecated after django 1.6+)
# python manage.py test <appname>.test:<TestCaseClass>.<TestMethod>