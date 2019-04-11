from django.db import models
from django.db.models import Model

class TecnicoModel(models, Model):

    nome = models.CharField(max_length=130)

    def __unicode__(self):
        return self.nome

    def __str__(self):
        return self.nome