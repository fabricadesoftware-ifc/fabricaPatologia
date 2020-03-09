# coding=utf-8
from django.db import models

from .cidade_model import CidadeModel

class BairroModel(models.Model):
    nome_bairro = models.CharField(max_length=100)
    id_cidade = models.ForeignKey(CidadeModel, on_delete=models.PROTECT)

    def __unicode__(self):
        return self.nome_bairro

    def __str__(self):
        return self.nome_bairro

    class Meta:
        verbose_name = "Bairro"
        verbose_name_plural = "Bairros"