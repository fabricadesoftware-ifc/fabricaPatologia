from django.forms import ModelForm

from laudosMedvet.models import RegiaoEstadoModel

class RegiaoEstadoForm(ModelForm):
    class Meta():
        model = RegiaoEstadoModel
        fields = ['id_estado', 'nome_regiao']