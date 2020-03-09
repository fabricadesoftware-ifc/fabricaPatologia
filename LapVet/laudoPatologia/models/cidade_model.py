# coding=utf-8
from django.db import models
from .estado_model import EstadoModel


class CidadeModel(models.Model):
    id_estado = models.ForeignKey(EstadoModel, on_delete=models.PROTECT)
    nome_cidade = models.CharField(max_length=100)

    def __unicode__(self):
        return self.nome_cidade

    def __str__(self):
        return self.nome_cidade

    class Meta:
        verbose_name = "Cidade"
        verbose_name_plural = "Cidades"
