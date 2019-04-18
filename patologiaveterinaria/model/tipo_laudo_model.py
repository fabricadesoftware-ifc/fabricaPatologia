from django.db import models

class TipoLaudoModel(models.Model):
    tipo = especie = (('0','--- Tipo de Laudo ---',),('1','Biópsia',), ('2','Citopatológico',),
                      ('3','Histopatológico',), ('4', 'Necropsia'))