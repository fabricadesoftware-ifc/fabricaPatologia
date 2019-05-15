from django.db import models
from laudosMedvet.models.regiao_federal_model import RegiaoFederalModel

class EstadoModel(models.Model):
    id_regiao_federal = models.ForeignKey(RegiaoFederalModel, on_delete=models.PROTECT)
    nome_estado = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.nome_estado