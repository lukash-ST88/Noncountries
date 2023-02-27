from .serializers import CountrySerializer
from .models import Country, Language, City
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response


class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

    @action(methods=['get'], detail=False)
    def languages(self, requset):
        langs = Language.objects.all()
        return Response({'languages': [lang.name for lang in langs]})

    @action(methods=['get'], detail=False)
    def cities(self, requset):
        cities = City.objects.all()
        return Response({'languages': [city.name for city in cities]})

    @action(methods=['get'], detail=True)
    def cats(self, request, pk):
        cat_countries = Country.objects.filter(cat__slug=pk)
        return Response({'cat_countries': [country.name for country in cat_countries]})
