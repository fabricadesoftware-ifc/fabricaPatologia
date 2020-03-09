# coding=utf-8
from django.db import models

from . import AnimalModel
from .tipo_laudo_model import TipoLaudoModel
from ckeditor.fields import RichTextField

#from .animal import AnimalModel
from .animal_model import AnimalModel


class RequisicaoLaudoModel(models.Model):
    rghv = models.IntegerField(blank=True, null=True)  #Fixme: models.Charfield() composto por tipolaudo[:2] + numero
    id_animal = models.ForeignKey(AnimalModel, on_delete=models.PROTECT)
    tipo_de_laudo = models.ForeignKey(TipoLaudoModel, on_delete=models.PROTECT)
    dt_coleta = models.DateField()
    material_enviado = RichTextField()
    historico_clinico = RichTextField()
    descricao_macroscopica = RichTextField()
    scan_figura_ficha_clinica = models.ImageField(upload_to='imagem_ficha_clinica', blank=True)
    responsavel_recebimento = models.CharField(max_length=100, blank=True)
    dt_recebimento = models.DateField()

    def __unicode__(self):
        return str(self.id) + ' , ' + str(self.tipo_de_laudo.nome_tipo_laudo) +' , '+ str(self.id_animal.nome_animal)

    def __str__(self):
        return str(self.id) + ' , ' + str(self.tipo_de_laudo.nome_tipo_laudo) +' , '+ str(self.id_animal.nome_animal)

    class Meta:
        verbose_name = "Requisição"
        verbose_name_plural = "Requisições"