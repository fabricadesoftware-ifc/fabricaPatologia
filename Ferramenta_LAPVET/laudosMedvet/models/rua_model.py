from django.db import models

from laudosMedvet.models.bairro_model import BairroModel

class RuaModel(models.Model):
    nome_rua = models.CharField(max_length=50)
    cep = models.CharField(max_length=40)
    id_bairro = models.ForeignKey(BairroModel, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome_rua