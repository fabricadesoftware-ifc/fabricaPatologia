from django.db import models

from laudosMedvet.models.especie_model import EspecieModel


class CadastrarAnimalModel(models.Model):
    nome = models.CharField(max_length=100)
    raca = models.CharField(max_length=100)
    dt_cadastro = models.DateTimeField(auto_now_add=True)
    sexo = (('M', 'Macho',), ('F', 'Fêmea'))
    especie = models.ForeignKey(EspecieModel, on_delete=models.CASCADE) # Chave estrangeira para especie_model
    proprietario = models.CharField(max_length=300)
    telefone_proprietario = models.CharField(max_length=100)
    veterinario_responsavel = models.CharField(max_length=300)
    telefone_veterinario_responsavel = models.CharField(max_length=100)


    def __unicode__(self):
        return self.nome

    def __str__(self):
        return self.raca


