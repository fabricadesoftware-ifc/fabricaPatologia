from django.db import models
from django.contrib.auth.models import Group

class PermissaoModel(models.Model):
    id_grupo = models.ManyToManyField(Group)
    class Meta:
        permissions = (
            ('pode_acessar_estado', 'Pode acessar estado'),
        )