from django.urls import path
from .views import CountryList, CountryDetail, about, CountryCategory, AddCountry, terminology, LoginUser, logout_user, \
    RegisterUser, SearchView, CountryListYearOrdering

urlpatterns = [
    path('', CountryList.as_view(), name='home'),
    path('country/<slug:country_slug>', CountryDetail.as_view(), name='detail'),
    path('about/', about, name='about'),
    path('category/<slug:cat_slug>', CountryCategory.as_view(), name='category'),
    path('add-country/', AddCountry.as_view(), name="add_country"),
    path('terminology/', terminology, name='terminology'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('search/', SearchView.as_view(), name='search'),
    path('sort/', CountryListYearOrdering.as_view(), name='sort'),
]
