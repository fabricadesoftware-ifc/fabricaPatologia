from django.db import models
from laudosMedvet.models.regiao_estado_model import RegiaoEstadoModel

class CidadeModel(models.Model):
    id_regiao_estado = models.ForeignKey(RegiaoEstadoModel, on_delete=models.PROTECT)
    nome_cidade = models.CharField(max_length=100)

    def __str__(self):
        return self.nome_cidade