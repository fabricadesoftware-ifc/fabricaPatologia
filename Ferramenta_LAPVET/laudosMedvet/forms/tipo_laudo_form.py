from django.forms import ModelForm

from laudosMedvet.models import TipoLaudoModel

class TipoLaudoForm(ModelForm):
    class Meta():
        model = TipoLaudoModel
        fields = ['tipo_laudo']