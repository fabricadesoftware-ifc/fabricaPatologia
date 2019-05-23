from django.db import models

class RegiaoFederalModel(models.Model):
    nome_regiao = models.CharField(max_length=20)

    class Meta:
        verbose_name = "Regiões Federais"
        verbose_name_plural = "Região Federal"

    def __str__(self):
        return self.nome_regiao