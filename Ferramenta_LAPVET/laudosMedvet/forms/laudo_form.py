from django.forms import ModelForm
from django import forms
from laudosMedvet.models import LaudoModel


class LaudoForm(ModelForm):

    class Meta():
        model = LaudoModel
        fields = ['id_requisicao', 'descricao_microscopica', 'diagnostico_morfologico', 'sistemas',
                  'etiologia', 'diagnostico_final', 'comentarios', 'veterinario_patologista','dt_laudo']