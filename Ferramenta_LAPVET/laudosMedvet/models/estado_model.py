from django.db import models
from laudosMedvet.models.regiao_federal_model import RegiaoFederalModel

class EstadoModel(models.Model):
    id_regiao_federal = models.ForeignKey(RegiaoFederalModel, on_delete=models.PROTECT)
    uf = models.CharField(max_length=2, primary_key=True)
    nome_estado = models.CharField(max_length=100)

    def __str__(self):
        return self.nome_estado