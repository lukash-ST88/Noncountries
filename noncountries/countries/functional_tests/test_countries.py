from selenium import webdriver
from countries.models import Country, Category, City, Language
from django.urls import reverse
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

from selenium.webdriver.common.by import By


class TestCountries(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome('functional_tests/chromedriver.exe')

    def tearDown(self):
        self.browser.close()

    def test_user_is_redirected_to_country_detail(self):
        country = Country.objects.create(name='Armini', original_name='army', slug='armin', area=1000,
                                         population=2.2, year=1991, description='strana takaya', reasons='h.z.',
                                         flag='countries/flags/Flag_of_Armenia.png',
                                         emblem='countries/emblems/Coat_of_arms_of_Armenia.png',
                                         map='countries/maps/armaniamap.png',
                                         anthem='countries/anthems/national_anthem_armenia.mp3',
                                         cat=Category.objects.create(name='cat1', slug='cat1slug'),
                                         capital=City.objects.create(name='cot)'))
        self.browser.get(self.live_server_url)

        country_detail = self.live_server_url + reverse('detail', args=[country.slug])
        self.browser.find_element(By.LINK_TEXT, country.name).click()
        self.assertEquals(self.browser.current_url, country_detail)

    def test_user_sees_sidebar_items(self):
        self.browser.get(self.live_server_url)
        sidebar = self.browser.find_element(by=By.ID, value='left-chapters').find_element(by=By.CLASS_NAME,
                                                                                          value='selected')
        self.assertEquals(sidebar.text, "Все категории")
