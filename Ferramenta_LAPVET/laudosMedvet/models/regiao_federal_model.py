from django.db import models

class RegiaoFederalModel(models.Model):
    nome_regiao = models.CharField(max_length=20)