from django.db import models

class SexoModel(models.Model):
    sexo = (('M', 'Macho',), ('F', 'Fêmea'))