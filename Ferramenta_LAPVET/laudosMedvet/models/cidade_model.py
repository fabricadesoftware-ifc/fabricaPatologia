from django.db import models
from laudosMedvet.models.estado_model import EstadoModel


class CidadeModel(models.Model):
    id_estado = models.ForeignKey(EstadoModel, on_delete=models.PROTECT)
    nome_cidade = models.CharField(max_length=100)

    def __str__(self):
        return self.nome_cidade