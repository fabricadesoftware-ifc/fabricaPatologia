from django.db import models

from patologiaveterinaria.model.estado_model import EstadoModel

class CidadeModel(models.Model):
    nome = models.CharField(max_length=128, null=False)


    def __unicode__(self):
        return self.nome

    def __str__(self):
        return self.nome

