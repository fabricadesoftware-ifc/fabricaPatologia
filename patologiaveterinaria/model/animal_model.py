from django.db import models
from django.db.models import Model
from patologiaveterinaria.model import EspecieModel


class AnimalModel(models,Model):
    nome = models.CharField(max_length=300, null=False)
    especie = models.ForeignKey(EspecieModel, blank=True, null=True)
    raca = models.CharField(max_length=100)
    sexo = models.CharField(max_length=5, blank=True)
    idade = models.CharField(max_length=30)

    def __str__(self):
        return self.nome

    def __str__(self):
        return self.raca

    def __str__(self):
        return self.idade
