from django.db import models
from django.urls import reverse


class Country(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    original_name = models.CharField(max_length=255, verbose_name='Оригинальное название')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    area = models.IntegerField(verbose_name='Площадь')
    population = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Население')
    year = models.IntegerField(verbose_name='Год основания')
    description = models.TextField(null=True, verbose_name='Описание')
    reasons = models.TextField(blank=True, verbose_name='Причины')
    flag = models.ImageField(upload_to='countries/flags/', verbose_name='Флаг')
    emblem = models.ImageField(upload_to='countries/emblems/', verbose_name='Герб')
    map = models.ImageField(upload_to='countries/maps/', verbose_name='Карта')
    anthem = models.FileField(null=True, upload_to='countries/anthems/', verbose_name='Гимн')
    cat = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, verbose_name='Категория')
    capital = models.OneToOneField('City', on_delete=models.SET_NULL, null=True, verbose_name='Столица')
    language = models.ManyToManyField('Language', verbose_name='Язык')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'country_slug': self.slug})


class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True, verbose_name='Категория')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='URL')

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=50, verbose_name='Язык')

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
