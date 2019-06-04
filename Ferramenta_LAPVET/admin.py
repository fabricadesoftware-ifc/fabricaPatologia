from django.contrib import admin

from laudosMedvet.models import EspecieModel, LaudoModel, AnimalModel

# Register your models here.


admin.site.register(EspecieModel)

admin.site.register(AnimalModel)

admin.site.register(LaudoModel)