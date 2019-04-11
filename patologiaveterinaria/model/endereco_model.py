from django.db import models
from django.db.models import Model

from patologiaveterinaria.model.estado_model import EstadoModel
from patologiaveterinaria.model.cidade_model import CidadeModel

class EnderecoModel(models, Model):
    rua = models.CharField(max_length=130, blank=True)
    bairro = models.CharField(max_length=130, blank=True)
    cep = models.CharField(max_length=9, blank=True)
    cidade = models.ForeignKey(CidadeModel, blank=True, null=True)