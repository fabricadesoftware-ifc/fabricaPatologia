from django.db import models
from django.db.models import Model

class ProprietarioModel(models,Model):
    nome = models.CharField(max_length=130, null=False)
    telefone = models.CharField(max_length=20, blank=True)
    endereco = models.CharField(max_length=128, blank=True)

    def __unicode__(self):
        return self.nome

    def __str__(self):
        return self.nome

    def __str__(self):
        return self.telefone

    def __str__(self):
        return self.endereco