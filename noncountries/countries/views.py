from django.shortcuts import render
from django.urls import reverse_lazy

from .forms import AddCountryForm
from .utils import menu, DataMixin
from django.views.generic import ListView, DetailView, CreateView
from .models import Country, Category


class CountryList(DataMixin, ListView):
    model = Country
    template_name = 'countries/index.html'
    context_object_name = 'countries'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        mixin_context = self.get_user_context(title='Главная страница')
        return dict(list(context.items()) + list(mixin_context.items()))


class CountryDetail(DataMixin, DetailView):
    model = Country
    template_name = 'countries/detail.html'
    slug_url_kwarg = 'country_slug'
    context_object_name = 'the_country'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        mixin_context = self.get_user_context(title=context['the_country'])
        return dict(list(context.items()) + list(mixin_context.items()))


class CountryCategory(DataMixin, ListView):
    model = Country
    template_name = 'countries/index.html'
    context_object_name = 'countries'
    allow_empty = False

    def get_queryset(self):
        return Country.objects.filter(cat__slug=self.kwargs['cat_slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c = Category.objects.get(slug=self.kwargs['cat_slug'])
        mixin_context = self.get_user_context(title='Категория - ' + str(c.name), cat_celected=c.pk)
        return dict(list(context.items()) + list(mixin_context.items()))


class AddCountry(DataMixin, CreateView):
    form_class = AddCountryForm
    template_name = 'countries/addcountry.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        mixin_context = self.get_user_context(title='Новая страна')
        return dict(list(context.items()) + list(mixin_context.items()))


def about(request):
    return render(request, 'countries/about.html', {'menu': menu, 'title': menu[0]['title']})


def terminology(request):
    return render(request, 'countries/terminology.html', {'menu': menu, 'title': menu[2]['title']})
