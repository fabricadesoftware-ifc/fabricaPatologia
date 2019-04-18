from django.db import models

class AnimalModel(models.Model):
    nome = models.CharField(max_length=130)
    idade = models.CharField(max_length=2)
    especie = (('0','--- Selecione a espécie ---',),('1','Mamífero',), ('2','Ave',),('3','Répil',), ('4', 'Peixe'))
    raca = models.CharField(max_length=100)
    pelagem = models.CharField(max_length=130)
    sexo = (('M', 'Macho',), ('F', 'Fêmea'))
    proprietario = models.CharField(max_length=130)
    telefone = models.CharField(max_length=11)
    veterinario_responsavel = models.CharField(max_length=130)
    telefone_vet = models.CharField(max_length=11)
    endereco = models.CharField(max_length=128, blank=True)
    numero_endereco = models.CharField(max_length=10, blank=True)
    bairro = models.CharField(max_length=128, blank=True)
    cep = models.CharField(max_length=9, blank=True)