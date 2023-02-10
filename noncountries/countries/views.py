from django.shortcuts import render
from .utils import *
from django.views.generic import ListView, DetailView, CreateView


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
