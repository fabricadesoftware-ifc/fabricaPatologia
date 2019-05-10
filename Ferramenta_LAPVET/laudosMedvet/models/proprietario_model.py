from django.db import models
from laudosMedvet.models.rua_model import RuaModel

class ProprietarioModel(models.Model):
    nome_proprietario = models.CharField(max_length=150)
    data_nasc = models.DateField('Data Nascimento')
    cpf = models.CharField(max_length=14)
    rg = models.CharField(max_length=15)
    telefone = models.CharField(max_length=40)
    celular = models.CharField(max_length=40, null=True)
    email = models.CharField(max_length=80)
    rua = models.ForeignKey(RuaModel, on_delete=models.PROTECT)
    numero = models.IntegerField()
    complemento = models.CharField(max_length=250, null=True)
