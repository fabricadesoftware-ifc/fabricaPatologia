# coding:utf-8
from django.forms import ModelForm
from ..models import LaudoModel


class LaudoForm(ModelForm):

    class Meta():
        model = LaudoModel
        fields = ['id_requisicao', 'descricao_microscopica', 'diagnostico_morfologico', 'sistemas',
                  'etiologia', 'diagnostico_final', 'comentarios', 'veterinario_patologista','dt_laudo']