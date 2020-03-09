# coding=utf-8
from django.db import models
from .requisicao_laudo_model import RequisicaoLaudoModel
from .veterinario_patologista_model import VeterinarioPatologistaModel
from multiselectfield import MultiSelectField
from ckeditor.fields import RichTextField


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
    descricao_microscopica = RichTextField()
    diagnostico_morfologico = RichTextField()
    sistemas = MultiSelectField(null=True, blank=True, choices=DATA_CHOICE)
    etiologia = models.CharField(max_length=300, null=True, blank=True)
    diagnostico_final = RichTextField(null=True, blank=True)
    comentarios = RichTextField()
    veterinario_patologista = models.ForeignKey(VeterinarioPatologistaModel, on_delete=models.PROTECT)
    dt_laudo = models.DateField()

    def __unicode__(self):
        return str(self.id_requisicao)

    def __str__(self):
        return str(self.id_requisicao)

    class Meta:
        verbose_name = "Laudo"
        verbose_name_plural = "Laudos"