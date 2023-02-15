from django.test import SimpleTestCase
from django.urls import resolve, reverse
from countries.views import *


class TestUrls(SimpleTestCase):
    """тестирование url адресов с представлениями функциями, классами """

    def test_about_url_is_resolves(self):
        url = reverse('about')
        print(resolve(url))
        self.assertEquals(resolve(url).func, about)

    def test_add_country_url_is_resolves(self):
        url = reverse('add_country')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, AddCountry)

    def test_detail_url_resolves(self):
        url = reverse('detail', args=['some-slug'])
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, CountryDetail)
