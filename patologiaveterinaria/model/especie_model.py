from django.db import models
from django.db.models import Model

class EspecieModel(models,Model):

    especie = models.CharField(max_length=30, unique=True)

    def __unicode__(self):
        return self.especie

    def __str__(self):
        return self.especie