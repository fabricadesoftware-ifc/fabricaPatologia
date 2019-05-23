from django.db import models
from laudosMedvet.models.requisicao_laudo_model import RequisicaoLaudoModel

class LaudoModel(models.Model):
    id_requisicao = models.OneToOneField(RequisicaoLaudoModel, on_delete=models.CASCADE)
    descricao_microscopica = models.TextField()
    diagnostico_morfologico = models.TextField()
    diagnostico_final = models.TextField(null=True, blank=True)
    comentarios = models.TextField()
    dt_laudo = models.DateField()

    def __str__(self):
        return 'Laudo nº: ' + str(self.id) + ' Data: ' + str(self.dt_laudo)
