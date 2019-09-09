from django.db import models
from laudosMedvet.models.tipo_laudo_model import TipoLaudoModel
from laudosMedvet.models.animal_model import AnimalModel

class RequisicaoLaudoModel(models.Model):
    rghv = models.IntegerField(blank=True, null=True)  #Fixme: models.Charfield() composto por tipolaudo[:2] + numero
    cod_animail = models.ForeignKey(AnimalModel, on_delete=models.PROTECT)
    tipo_de_laudo = models.ForeignKey(TipoLaudoModel, on_delete=models.PROTECT)
    dt_coleta = models.DateField()
    material_enviado = models.TextField()
    historico_clinico = models.TextField()
    descricao_macroscopica = models.TextField()
    scan_figura_ficha_clinica = models.ImageField(upload_to='imagem_ficha_clinica', blank=True)
    dt_recebimento = models.DateField()


    def __str__(self):
        return str(self.id)