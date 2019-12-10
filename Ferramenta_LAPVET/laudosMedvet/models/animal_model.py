from django.db import models

from laudosMedvet.models.especie_model import EspecieModel
from laudosMedvet.models.raca_model import RacaModel
from laudosMedvet.models.proprietario_model import ProprietarioModel
from laudosMedvet.models.veterinario_responsavel_model import VeterinarioResponsavelModel
from laudosMedvet.models.rua_model import RuaModel
from laudosMedvet.models.bairro_model import BairroModel
from laudosMedvet.models.cidade_model import CidadeModel
from laudosMedvet.models.estado_model import EstadoModel


class AnimalModel(models.Model):
    nome = models.CharField(max_length=100, blank=True, null=True)
    idade = models.CharField(max_length=50, blank=True, null=True)
    sexo = models.CharField(max_length=5, blank=True, null=True)
    id_especie = models.ForeignKey(EspecieModel, on_delete=models.PROTECT, null=True)
    raca = models.ForeignKey(RacaModel, on_delete=models.PROTECT, blank=True, null=True)
    cor_pelagem = models.CharField(max_length=50, blank=True)
    dt_cadastro = models.DateField(auto_now_add=True)
    proprietario = models.ForeignKey(ProprietarioModel, on_delete=models.PROTECT, blank=True, null=True)
    veterinario_responsavel = models.ForeignKey(VeterinarioResponsavelModel,
                                                on_delete=models.PROTECT, blank=True, null=True)
    id_estado = models.ForeignKey(EstadoModel, on_delete=models.PROTECT, blank=True, null=True)
    cidade = models.ForeignKey(CidadeModel, on_delete=models.PROTECT, blank=True, null=True)
    bairro = models.ForeignKey(BairroModel, on_delete=models.PROTECT, blank=True, null=True)
    rua = models.ForeignKey(RuaModel, on_delete=models.PROTECT, blank=True, null=True)
    numero = models.PositiveIntegerField(default=0)
    complemento = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        verbose_name = "Animal"
        verbose_name_plural = "Animais"

    def __str__(self):
        return str(self.id) + ', ' + self.nome

