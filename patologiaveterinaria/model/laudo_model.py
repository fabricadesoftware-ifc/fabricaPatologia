from django.db import models

class LaudoModel(models.Model):
    historico_clinico = models.CharField(max_length=3000)
    descricao_macroscopica = models.CharField(max_length=3000)
    descricao_microscopica = models.CharField(max_length=3000)
    diagnostico_morfologico = models.CharField(max_length=3000)
    comentarios = models.CharField(max_length=3000)
