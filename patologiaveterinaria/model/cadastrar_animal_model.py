from django.db import models

class AnimalModel(models.Model):

    nome = models.CharField(max_length=130)
    idade = models.CharField(max_length=2)
    raca = models.CharField(max_length=100)
    pelagem = models.CharField(max_length=130)
    proprietario = models.CharField(max_length=130)
    telefone = models.CharField(max_length=11)
    veterinario_responsavel = models.CharField(max_length=130)
    telefone_vet = models.CharField(max_length=11)
    endereco = models.CharField(max_length=128, blank=True)
    numero_endereco = models.CharField(max_length=10, blank=True)
    bairro = models.CharField(max_length=128, blank=True)
    cep = models.CharField(max_length=9, blank=True)
    data_cadastro_animal = models.DateTimeField(auto_now_add=True)

