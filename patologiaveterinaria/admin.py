from django.contrib import admin
from .model import TipoLaudoModel, EspecieModel, AnimalModel, LaudoModel

admin.site.register(TipoLaudoModel)

admin.site.register(EspecieModel)

admin.site.register(AnimalModel)

admin.site.register(LaudoModel)