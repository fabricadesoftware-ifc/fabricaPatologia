# coding=utf-8
from django.contrib import admin
from .models import (TipoLaudoModel, EstadoModel, CidadeModel, BairroModel, RuaModel, ProprietarioModel,
                     VeterinarioResponsavelModel, EspecieModel, RacaModel, AnimalModel, RequisicaoLaudoModel,
                     VeterinarioPatologistaModel, LaudoModel, ImagensModel)
# Register your models here.

admin.site.register(TipoLaudoModel)
admin.site.register(RequisicaoLaudoModel)
admin.site.register(EstadoModel)
admin.site.register(CidadeModel)
admin.site.register(BairroModel)
admin.site.register(RuaModel)
admin.site.register(ProprietarioModel)
admin.site.register(VeterinarioResponsavelModel)
admin.site.register(EspecieModel)
admin.site.register(RacaModel)
admin.site.register(AnimalModel)
admin.site.register(VeterinarioPatologistaModel)
admin.site.register(LaudoModel)
admin.site.register(ImagensModel)
