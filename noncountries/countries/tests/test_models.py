from django.test import TestCase
from countries.models import Category

class TestModels(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.cat1 = Category.objects.create(name='временные государства', slug='temporary-states')

    def test_category_get_absolute_url(self):
        self.assertEqual(self.cat1.get_absolute_url(), '/category/temporary-states')