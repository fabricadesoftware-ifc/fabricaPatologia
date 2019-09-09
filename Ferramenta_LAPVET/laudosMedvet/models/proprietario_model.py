from django.db import models
from laudosMedvet.models.rua_model import RuaModel

class ProprietarioModel(models.Model):
    nome_proprietario = models.CharField(max_length=150)
    data_nasc = models.DateField('Data Nascimento', blank=True, null=True)
    cpf = models.CharField(max_length=14, blank=True, null=True)
    rg = models.CharField(max_length=15, blank=True, null=True)
    telefone = models.CharField(max_length=40, blank=True, null=True)
    celular = models.CharField(max_length=40, null=True, blank=True)
    email = models.CharField(max_length=80, blank=True, null=True)
    rua = models.ForeignKey(RuaModel, on_delete=models.PROTECT, blank=True, null=True)
    numero = models.IntegerField(blank=True, null=True)
    complemento = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.nome_proprietario
