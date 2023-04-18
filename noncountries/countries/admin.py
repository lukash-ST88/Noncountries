from django.contrib import admin
from .models import *

admin.site.register(Country)
admin.site.register(Language)
admin.site.register(Category)
admin.site.register(City)

#TODO: сделать возможность множественного добавления в модели
#TODO: REST сделать расписанным для сериализации
