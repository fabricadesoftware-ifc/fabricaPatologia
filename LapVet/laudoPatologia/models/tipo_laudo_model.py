# coding=utf-8
from django.db import models

class TipoLaudoModel(models.Model):
    nome_tipo_laudo = models.CharField(max_length=100)

    def __unicode__(self):
        return self.nome_tipo_laudo

    def __str__(self):
        return self.nome_tipo_laudo

    class Meta:
        verbose_name = "Tipo de Laudo"
        verbose_name_plural = "Tipos de Laudo"