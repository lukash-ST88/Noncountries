from django.urls import path
from .views import *

urlpatterns = [
    path('', CountryList.as_view(), name='home'),
    path('country/<slug:country_slug>', CountryDetail.as_view(), name='detail'),
    path('about/', about, name='about'),
    path('category/<slug:cat_slug>', CountryCategory.as_view(), name='category'),
    path('add-country/', AddCountry.as_view(), name="add_country"),
    path('terminology/', terminology, name='terminology')
    ]
