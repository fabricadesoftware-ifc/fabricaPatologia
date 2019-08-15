from django.db import models
from laudosMedvet.models.requisicao_laudo_model import RequisicaoLaudoModel

class LaudoModel(models.Model):
    id_requisicao = models.OneToOneField(RequisicaoLaudoModel, on_delete=models.CASCADE)
    descricao_microscopica = models.TextField()
    diagnostico_morfologico = models.TextField()
    sistemas = models.CharField(max_length=50)
    etiologia = models.CharField(max_length=300, blank=True)
    diagnostico_final = models.TextField(null=True, blank=True)
    comentarios = models.TextField()
    dt_laudo = models.DateField()

    def __str__(self):
        return str(self.id_requisicao)