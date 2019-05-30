from django.forms import ModelForm

from laudosMedvet.models import RequisicaoLaudoModel

class RequisicaoLaudoForm(ModelForm):
    class Meta():
        model = RequisicaoLaudoModel
        fields = ['cod_animail', 'tipo_de_laudo', 'dt_coleta', 'material_enviado', 'historico_clinico',
                  'descricao_macroscopica', 'dt_recebimento']