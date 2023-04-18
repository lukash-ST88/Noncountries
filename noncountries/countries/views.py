from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import AddCountryForm, LoginUserForm, RegisterUserForm, OrderingForm
from .utils import menu, DataMixin
from django.views.generic import ListView, DetailView, CreateView, FormView
from .models import Country, Category
from django.views.decorators.cache import cache_page


class CountryList(DataMixin, FormView, ListView):
    model = Country
    template_name = 'countries/index.html'
    context_object_name = 'countries'
    form_class = OrderingForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        mixin_context = self.get_user_context(title='Главная страница')
        return dict(list(context.items()) + list(mixin_context.items()))

    def get_queryset(self, *args, **kwargs):
        return Country.objects.all().select_related('cat')


class CountryDetail(DataMixin, DetailView):
    model = Country
    template_name = 'countries/detail.html'
    slug_url_kwarg = 'country_slug'
    context_object_name = 'the_country'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        mixin_context = self.get_user_context(title=context['the_country'])
        return dict(list(context.items()) + list(mixin_context.items()))


class CountryCategory(DataMixin, FormView, ListView):
    model = Country
    template_name = 'countries/index.html'
    context_object_name = 'countries'
    allow_empty = False
    form_class = OrderingForm

    def get_queryset(self):
        return Country.objects.filter(cat__slug=self.kwargs['cat_slug']).select_related('cat')

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


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'countries/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        mixin_context = self.get_user_context(title='Авторизация')
        return dict(list(context.items()) + list(mixin_context.items()))

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')


class RegisterUser(DataMixin, CreateView):  # django crispy forms
    form_class = RegisterUserForm
    template_name = 'countries/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        mixin_context = self.get_user_context(title='Регистрация')
        return dict(list(context.items()) + list(mixin_context.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class SearchView(DataMixin, FormView, ListView):
    """класс отображения результатов поисковой строки"""
    template_name = 'countries/index.html'
    context_object_name = 'countries'
    form_class = OrderingForm

    def get_queryset(self):
        return Country.objects.filter(name__icontains=self.request.GET.get('q')).select_related('cat')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        mixin_context = self.get_user_context(title='Результат поиска', q=f"q={self.request.GET.get('q')}&")
        return dict(list(context.items()) + list(mixin_context.items()))


class CountryListYearOrdering(DataMixin, FormView, ListView):
    """класс представления отсортированного списка"""
    template_name = 'countries/index.html'
    context_object_name = 'countries'
    form_class = OrderingForm

    def get_queryset(self):
        return Country.objects.all().order_by(self.request.GET.get('ordering')).select_related('cat')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        mixin_context = self.get_user_context(title='Сортировка по году',
                                              ord=f"ordering={self.request.GET.get('ordering')}&")
        return dict(list(context.items()) + list(mixin_context.items()))


def about(request):
    return render(request, 'countries/about.html', {'menu': menu, 'title': menu[0]['title']})


def terminology(request):
    return render(request, 'countries/terminology.html', {'menu': menu, 'title': menu[2]['title']})
