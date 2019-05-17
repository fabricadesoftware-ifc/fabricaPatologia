from django.db import models

from laudosMedvet.models.especie_model import EspecieModel
from laudosMedvet.models.proprietario_model import ProprietarioModel
from laudosMedvet.models.veterinario_responsavel_model import VeterinarioresponsavelModel
from laudosMedvet.models.rua_model import RuaModel


class AnimalModel(models.Model):
    nome = models.CharField(max_length=100)
    data_nasc = models.DateField('Data de nascimento')
    sexo = models.CharField(max_length=1, default=None)
    raca = models.CharField(max_length=100)
    cor_pelagem = models.CharField(max_length=50)
    especie = models.ForeignKey(EspecieModel, on_delete=models.PROTECT) # Chave estrangeira para especie_model
    dt_cadastro = models.DateTimeField(auto_now_add=True)
    proprietario = models.ForeignKey(ProprietarioModel, on_delete=models.PROTECT)
    veterinario_responsavel = models.ForeignKey(VeterinarioresponsavelModel, on_delete=models.PROTECT)
    rua = models.ForeignKey(RuaModel, on_delete=models.PROTECT)


    def __unicode__(self):
        return self.nome

    def __str__(self):
        return self.raca
