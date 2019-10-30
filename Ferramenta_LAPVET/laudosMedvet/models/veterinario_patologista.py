from django.db import models


class VeterinarioPatologistaModel(models.Model):
    nome = models.CharField(max_length=150)
    formacao = models.CharField(max_length=150)
    crmv = models.CharField(max_length=20)

    def __str__(self):
        return self.nome