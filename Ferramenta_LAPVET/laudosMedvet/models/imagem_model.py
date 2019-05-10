from django.db import models
from laudosMedvet.models.laudo_model import LaudoModel


class ImagensModel(models.Model):
    descricao_imagem = models.CharField(max_length=150)
    imagem = models.ImageField(upload_to='imagens', null=True, blank=True)
    id_model = models.ForeignKey(LaudoModel, on_delete=models.CASCADE)


    def __str__(self):
        return self.descricao_imagem
