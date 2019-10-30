from django.contrib import admin

from laudosMedvet.models import EspecieModel, LaudoModel, AnimalModel, RequisicaoLaudoModel, RacaModel,\
    UsuarioModel, VeterinarioPatologistaModel

# Register your models here.


admin.site.register(EspecieModel)

admin.site.register(AnimalModel)
admin.site.register(RacaModel)
admin.site.register(VeterinarioPatologistaModel)
admin.site.register(LaudoModel)
admin.site.register(RequisicaoLaudoModel)
admin.site.register(UsuarioModel)