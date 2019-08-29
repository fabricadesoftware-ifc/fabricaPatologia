from django.db import models

from laudosMedvet.models.especie_model import EspecieModel
from laudosMedvet.models.raca_model import RacaModel
from laudosMedvet.models.proprietario_model import ProprietarioModel
from laudosMedvet.models.veterinario_responsavel_model import VeterinarioResponsavelModel
from laudosMedvet.models.rua_model import RuaModel


class AnimalModel(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    sexo = models.CharField(max_length=5, default=None)
    raca = models.ForeignKey(RacaModel, on_delete=models.PROTECT)  # Chave estrangeira para raça_model --> especie
    cor_pelagem = models.CharField(max_length=50)
    dt_cadastro = models.DateField(auto_now_add=True)
    proprietario = models.ForeignKey(ProprietarioModel, on_delete=models.PROTECT)
    veterinario_responsavel = models.ForeignKey(VeterinarioResponsavelModel, on_delete=models.PROTECT, blank=True, null=True)
    rua = models.ForeignKey(RuaModel, on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Animal"
        verbose_name_plural = "Animais"

    def __str__(self):
        return str(self.id) + ', ' + self.nome + ', ' + self.raca.nome_raca

