from django.contrib import admin

from .models import EspecieModel, TipoLaudoModel, LaudoModel, ImagensModel


admin.site.register(EspecieModel)


admin.site.register(TipoLaudoModel)

admin.site.register(LaudoModel)

admin.site.register(ImagensModel)