# coding=utf-8
from django.db import models


class VeterinarioResponsavelModel(models.Model):
    nome_veterinario = models.CharField(max_length=150, blank=True, null=True)
    telefone = models.CharField(max_length=40, blank=True, null=True)
    crmv = models.CharField(max_length=20, blank=True, null=True)

    def __unicode__(self):
        return self.nome_veterinario

    def __str__(self):
        return self.nome_veterinario

    class Meta:
        verbose_name = "Veterinário Responsável"
        verbose_name_plural = "Veterinários Responsáveis"