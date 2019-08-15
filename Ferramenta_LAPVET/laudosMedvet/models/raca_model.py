from django.db import models
from laudosMedvet.models.especie_model import EspecieModel

class RacaModel(models.Model):
    nome_raca = models.CharField(max_length=100)
    id_especie = models.ForeignKey(EspecieModel, on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Raça"
        verbose_name_plural = "Raças"

    def __str__(self):
        return self.nome_raca