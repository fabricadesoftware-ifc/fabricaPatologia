from django.contrib import admin

from .models import EspecieModel, AnimalModel, ProprietarioModel, VeterinarioresponsavelModel, CidadeModel, RegiaoEstadoModel, EstadoModel, RegiaoFederalModel, BairroModel, RuaModel

admin.site.register(EspecieModel)

admin.site.register(ProprietarioModel)

admin.site.register(AnimalModel)

admin.site.register(VeterinarioresponsavelModel)

admin.site.register(CidadeModel)

admin.site.register(RegiaoEstadoModel)

admin.site.register(EstadoModel)

admin.site.register(RegiaoFederalModel)

admin.site.register(RuaModel)

admin.site.register(BairroModel)