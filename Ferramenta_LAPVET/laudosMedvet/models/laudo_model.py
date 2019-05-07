from django.db import models
from laudosMedvet.models.tipo_laudo_model import TipoLaudoModel
from laudosMedvet.models.imagem_model import ImagensModel


class LaudoModel(models.Model):
    tipo_laudo = models.ForeignKey(TipoLaudoModel, on_delete=models.CASCADE)
    material_enviado = models.CharField(max_length=500)
    imagens = models.ForeignKey(ImagensModel, on_delete=models.CASCADE)
    historico_clinico = models.TextField()
    descricao_macroscopica = models.TextField()
    descricao_microscopica = models.TextField()    #<<<<<-------orgaos
    diagnostico_morfologico = models.TextField()
    comentarios = models.TextField()

