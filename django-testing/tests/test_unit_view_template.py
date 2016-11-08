from django.test import TestCase
from django.http import HttpRequest
from animals.views import Animal


class HomePageTest(TestCase):
    def test_home_page_returns_correct_html(self):
        request = HttpRequest()  #
        response = Animal(request)  #
        self.assertTrue(response.content.startswith('<html>'))  #
        self.assertIn('<title>To-Do lists</title>', response.content)  #
        self.assertTrue(response.content.endswith('</html>'))  #

    def test_another_view(self):
        pass

"""
# procedure
In the terminal, run the unit tests and see how they fail
In the editor, make a minimal code change to address the current test failure
"""