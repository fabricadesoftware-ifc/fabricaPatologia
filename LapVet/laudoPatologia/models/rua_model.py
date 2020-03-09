# coding=utf-8
from django.db import models

from .bairro_model import BairroModel

class RuaModel(models.Model):
    nome_rua = models.CharField(max_length=50)
    cep = models.CharField(max_length=9)
    id_bairro = models.ForeignKey(BairroModel, on_delete=models.PROTECT)

    def __unicode__(self):
        return self.nome_rua

    def __str__(self):
        return self.nome_rua

    class Meta:
        verbose_name = "Rua"
        verbose_name_plural = "Ruas"