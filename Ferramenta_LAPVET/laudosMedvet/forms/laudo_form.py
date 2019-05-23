from django.forms import ModelForm

from laudosMedvet.models import LaudoModel

class LaudoForm(ModelForm):
    class Meta():
        model = LaudoModel
        fields = ['id_requisicao', 'descricao_microscopica', 'diagnostico_morfologico',
                  'diagnostico_final', 'comentarios', 'dt_laudo']