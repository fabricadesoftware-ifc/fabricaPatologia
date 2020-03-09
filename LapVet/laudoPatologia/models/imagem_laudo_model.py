# coding=utf-8
from django.db import models
from .laudo_model import LaudoModel


class ImagensModel(models.Model):
    nome_imagem = models.CharField(max_length=150)
    imagem = models.ImageField(upload_to='imagens')
    id_laudo = models.ForeignKey(LaudoModel, on_delete=models.PROTECT)

    def __unicode__(self):
        return self.nome_imagem

    def __str__(self):
        return self.nome_imagem

    class Meta:
        verbose_name = "Imagem"
        verbose_name_plural = "Imagens"