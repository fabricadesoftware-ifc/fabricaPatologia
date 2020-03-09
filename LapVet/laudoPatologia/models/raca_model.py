# coding=utf-8
from django.db import models
from .especie_model import EspecieModel


class RacaModel(models.Model):
    nome_raca = models.CharField(max_length=100)
    id_especie = models.ForeignKey(EspecieModel, on_delete=models.PROTECT)

    def __unicode__(self):
        return self.nome_raca

    def __str__(self):
        return self.nome_raca

    class Meta:
        verbose_name = "Raça"
        verbose_name_plural = "Raças"