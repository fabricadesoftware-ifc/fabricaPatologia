from django.db import models
from laudosMedvet.models.estado_model import EstadoModel

class RegiaoEstadoModel(models.Model):
    id_estado = models.ForeignKey(EstadoModel, on_delete=models.PROTECT)
    nome_regiao = models.CharField(max_length=50)

    def __str__(self):
        return self.nome_regiao