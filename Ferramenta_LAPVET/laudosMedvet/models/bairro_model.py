from django.db import models

from laudosMedvet.models.cidade_model import CidadeModel

class BairroModel(models.Model):
    nome_bairro = models.CharField(max_length=100)
    id_cidade = models.ForeignKey(CidadeModel, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome_bairro