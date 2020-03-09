# coding=utf-8
from django.db import models


class ProprietarioModel(models.Model):
    nome_proprietario = models.CharField(max_length=150)
    data_nasc = models.DateField('Data Nascimento', blank=True, null=True)
    cpf = models.CharField(max_length=14, blank=True, null=True)
    rg = models.CharField(max_length=15, blank=True, null=True)
    telefone = models.CharField(max_length=40, blank=True, null=True)
    celular = models.CharField(max_length=40, null=True, blank=True)
    email = models.CharField(max_length=80, blank=True, null=True)
    endereco = models.CharField(max_length=300, blank=True, null=True)
    numero = models.IntegerField(blank=True, null=True)
    complemento = models.CharField(max_length=250, null=True, blank=True)

    def __unicode__(self):
        return self.nome_proprietario

    def __str__(self):
        return self.nome_proprietario

    class Meta:
        verbose_name = "Proprietario"
        verbose_name_plural = "Proprietarios"