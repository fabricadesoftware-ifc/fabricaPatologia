from django.forms import ModelForm

from ..models import TipoLaudoModel

class TipoLaudoForm(ModelForm):
    class Meta():
        model = TipoLaudoModel
        fields = ['nome_tipo_laudo']