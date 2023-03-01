from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, Client
from django.urls import reverse
from countries.models import Country, Category, City, Language


class TestView(TestCase):

    def setUp(self):
        self.client = Client()
        self.country_list = reverse('home')
        self.country_detail = reverse('detail', args=['armin'])
        self.add_country = reverse('add_country')
        self.cat = Category.objects.create(name='cat1', slug='cat1slug')
        self.country = Country.objects.create(name='Armini', original_name='army', slug='armin', area=1000,
                                              population=2.2, year=1991, description='strana takaya', reasons='h.z.',
                                              flag='countries/flags/Flag_of_Armenia.png',
                                              emblem='countries/emblems/Coat_of_arms_of_Armenia.png',
                                              map='countries/maps/armaniamap.png',
                                              anthem='countries/anthems/national_anthem_armenia.mp3',
                                              cat=self.cat,
                                              capital=City.objects.create(name='cot)'))
        self.language = Language.objects.create(name='language1')

    def test_country_list_GET(self):
        response = self.client.get(self.country_list)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'countries/index.html')

    def test_country_detail_GET(self):
        response = self.client.get(self.country_detail)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'countries/detail.html')

    # def test_country_add_POST(self):
    #     self.city = City.objects.create(name='city1')
    #     self.flag = SimpleUploadedFile("countries/flags/Flag_of_Armenia.png", content=b'file_content',
    #                                    content_type="image/png")
    #     self.emblem = SimpleUploadedFile("countries/emblems/Coat_of_arms_of_Armenia.png", content=b'file_content',
    #                                      content_type="image/png")
    #     self.anthem = SimpleUploadedFile("countries/anthems/national_anthem_armenia.mp3", content=b'file_content',
    #                                      content_type="audio/mp3")
    #     self.map = SimpleUploadedFile("countries/maps/armaniamap.png", content=b'file_content',
    #                                   content_type="image/png")
    #
    #     # with open('countries/maps/armaniamap.png') as self.map, open(
    #     #         'countries/anthems/national_anthem_armenia.mp3') as self.anthem, open(
    #     #     'countries/emblems/Coat_of_arms_of_Armenia.png') as self.emblem, open(
    #     #     'countries/flags/Flag_of_Armenia.png') as self.flag:
    #     response = self.client.post(self.add_country, data={
    #         'name': 'Aountry1',
    #         'original_name': 'country1-origin',
    #         'slug': 'country1-slug',
    #         'description': 'something',
    #         'reasons':'something',
    #         'area': 2000,
    #         'population': 2.2,
    #         'flag': self.flag,
    #         'emblem': self.emblem,
    #         'map': self.map,
    #         'anthem': self.anthem,
    #         'cat': self.cat,
    #         'capital': self.city,
    #         'year': 2000,
    #         'language': (self.language,)
    #     })
    #     print('flag:', self.flag, self.anthem, self.language, sep='\n')
    #     print(Country.objects.all(), response)
    #     self.assertEquals(response.status_code, 200)
    #     self.assertEqual(Country.objects.get(name='Aountry1').name, 'Aountry1')
