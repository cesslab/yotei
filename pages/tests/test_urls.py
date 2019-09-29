from django.test import SimpleTestCase
from django.urls import reverse, resolve

from pages.views import HomePageView


class TestUrls(SimpleTestCase):
    def test_home_is_resolved(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
