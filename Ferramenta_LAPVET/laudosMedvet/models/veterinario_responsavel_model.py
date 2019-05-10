from django.db import models

class VeterinarioresponsavelModel(models.Model):
    nome_veterinario = models.CharField(max_length=150, blank=True, null=True)
    telefone = models.CharField(max_length=40, blank=True, null=True)
    crmv = models.CharField(max_length=20, blank=True, null=True)