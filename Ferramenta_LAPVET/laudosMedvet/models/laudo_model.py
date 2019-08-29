from django.db import models
from laudosMedvet.models.requisicao_laudo_model import RequisicaoLaudoModel
from multiselectfield import MultiSelectField

class LaudoModel(models.Model):
    DATA_CHOICE =(
        ('Cardiovascular', 'Cardiovascular'),
        ('Pulmonar', 'Pulmonar'),
        ('Digestivo', 'Digestivo'),
        ('Endócrino', 'Endócrino'),
        ('Nervoso', 'Nervoso'),
        ('Reprodutivo', 'Reprodutivo'),
        ('Muscular', 'Muscular'),
        ('Esquelético', 'Esquelético'),
        ('Tegumentar', 'Tegumentar'),
        ('Excretor', 'Excretor')
    )
    id_requisicao = models.OneToOneField(RequisicaoLaudoModel, on_delete=models.CASCADE)
    descricao_microscopica = models.TextField()
    diagnostico_morfologico = models.TextField()
    sistemas = MultiSelectField(null=True, blank=True, choices=DATA_CHOICE)
    etiologia = models.CharField(max_length=300, null=True)
    diagnostico_final = models.TextField(null=True, blank=True)
    comentarios = models.TextField()
    dt_laudo = models.DateField()

    def __str__(self):
        return str(self.id_requisicao)