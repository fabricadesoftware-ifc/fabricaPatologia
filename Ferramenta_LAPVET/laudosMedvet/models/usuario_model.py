from django.contrib.auth.models import User
from django.db import models
from laudosMedvet.models.cidade_model import CidadeModel
from laudosMedvet.models.estado_model import EstadoModel

from django.contrib.auth.models import User


class UserModel(User):

    def __unicode__(self):
        return self.first_name

    def __str__(self):
        return self.first_name

class UsuarioModel(models.Model):

    data_nasc = models.DateField('Data Nascimento', blank=True)
    cpf = models.CharField(max_length=14, blank=True)
    rg = models.CharField(max_length=45, blank=True)
    telefone = models.CharField(max_length=45, blank=True)
    celular = models.CharField(max_length=45, blank=True)
    email = models.CharField(max_length=100, blank=True)
    endereco = models.CharField(max_length=300, blank=True)
    numero = models.IntegerField(blank=True)
    bairro = models.CharField(max_length=100, blank=True)
    cidade = models.CharField(max_length=100, blank=True)
    estado = models.CharField(max_length=100, blank=True)
    username = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.email
