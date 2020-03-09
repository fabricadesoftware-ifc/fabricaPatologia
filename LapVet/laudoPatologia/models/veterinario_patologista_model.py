# coding=utf-8
from django.db import models


class VeterinarioPatologistaModel(models.Model):
    nome_veterinario_patologista = models.CharField(max_length=150, blank=True, null=True)
    formacao = models.CharField(max_length=100, blank=True, null=True)
    crmv = models.CharField(max_length=20, blank=True, null=True)

    def __unicode__(self):
        return self.nome_veterinario_patologista

    def __str__(self):
        return self.nome_veterinario_patologista

    class Meta:
        verbose_name = "Veterinário Patologista"
        verbose_name_plural = "Veterinários Patologista"
