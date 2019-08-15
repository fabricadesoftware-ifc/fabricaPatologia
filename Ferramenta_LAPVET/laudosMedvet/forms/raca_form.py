from django.forms import ModelForm
from laudosMedvet.models import RacaModel


class RacaForm(ModelForm):
    class Meta():
        model = RacaModel
        fields = ['nome_raca', 'id_especie']