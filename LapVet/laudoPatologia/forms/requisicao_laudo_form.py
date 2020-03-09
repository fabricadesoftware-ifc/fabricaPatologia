from django.forms import ModelForm

from ..models import RequisicaoLaudoModel

class RequisicaoLaudoForm(ModelForm):
    class Meta():
        model = RequisicaoLaudoModel
        fields = ['rghv','id_animal', 'tipo_de_laudo', 'dt_coleta', 'material_enviado', 'historico_clinico',
                  'descricao_macroscopica', 'dt_recebimento', 'scan_figura_ficha_clinica',
                  'responsavel_recebimento']