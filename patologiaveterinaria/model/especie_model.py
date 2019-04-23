from django.db import models

class EspecieModel(models.Model):

    especie = (('', '--- Selecione a espécie ---',),
               (1, 'Mamífero',),
               (2, 'Ave',),
               (3, 'Répil',),
               (4, 'Peixe'))