from django.db import models
from laudosMedvet.models.tipo_laudo_model import TipoLaudoModel

class RequisicaoLaudoModel(models.Model):
    tipo_de_laudo = models.ForeignKey(TipoLaudoModel, on_delete=models.PROTECT)
    dt_coleta = models.DateField()
    material_enviado = models.TextField()
    historico_clinico = models.TextField()
    descricao_macroscopica = models.TextField()
    dt_recebimento = models.DateField()

    def __str__(self):
        return 'Requisição nº: ' + str(self.id) + ' Data recebimento: ' + str(self.dt_recebimento) + \
               ' Tipo: ' + str(self.tipo_de_laudo)