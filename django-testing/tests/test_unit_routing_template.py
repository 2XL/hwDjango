from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.test import TestCase
from animals.views import Animal


class HomePageTest(TestCase):
    def test_home_page_returns_correct_html(self):
        request = HttpRequest()

        response = Animal(request)
        self.assertTrue(response.content.startswith('<html>'))
        self.assertIn('<title>To-Do lists</title>', response.content)
        self.assertTrue(response.content.endswith('</html>'))

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, Animal)

"""
Run this
python manage.py test lists
"""