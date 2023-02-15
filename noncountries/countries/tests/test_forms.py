from django.test import SimpleTestCase
from countries.forms import *


class TestForms(SimpleTestCase):
    """тестирование формы сортировки стран по году"""

    def test_ordering_form_valid_data(self):
        form = OrderingForm(data={
            'ordering': 'year',
        })

        self.assertTrue(form.is_valid())
