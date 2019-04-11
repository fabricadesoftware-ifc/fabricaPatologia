from django.db import models

class PatologistaModel(models.Model):
    nome = models.CharField(max_length=130, null=False)


    def __unicode__(self):
        return self.nome
    def __str__(self):
        return self.nome