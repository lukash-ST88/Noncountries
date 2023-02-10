from .models import *
from django.db.models import Count

menu = [{'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Добавить страну', 'url_name': 'add_country'},
        {'title': 'Терминология', 'url_name': 'terminology'},
        ]


class DataMixin:
    """В Mixin класс для представлений добавляем меню сайта и кололичество записей для каждой категории"""
    paginate_by = 4

    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Category.objects.annotate(Count('country'))
        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(1)
        context['menu'] = user_menu
        context['cats'] = cats
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context
