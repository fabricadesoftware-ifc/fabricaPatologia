from django.db import models

class TipoLaudoModel(models.Model):
    tipo_laudo = models.CharField(max_length=100)

    def __str__(self):
        return self.tipo_laudo