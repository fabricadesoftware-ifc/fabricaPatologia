from django.db import models

class LaudoModel(models.Model):
    nome = models.CharField(max_length=130)
    idade = models.CharField(max_length=2)
    especie = models.CharField(max_length=100)