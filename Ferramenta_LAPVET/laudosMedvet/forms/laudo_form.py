from django.forms import ModelForm

from laudosMedvet.models import LaudoModel

class LaudoForm(ModelForm):

    class Meta:
        model = LaudoModel
        fields = ['material_enviado', 'historico_clinico', 'descricao_macroscopica',
                  'descricao_microscopica', 'diagnostico_morfologico', 'comentarios']