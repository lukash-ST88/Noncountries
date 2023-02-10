from django.urls import path
from .views import *

urlpatterns = [
    path('', CountryList.as_view(), name='home'),
    path('country/<slug:country_slug', CountryDetail.as_view(), name='detail')
    ]
