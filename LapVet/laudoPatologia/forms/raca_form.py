from django.forms import ModelForm
from ..models import RacaModel


class RacaForm(ModelForm):
    class Meta():
        model = RacaModel
        fields = ['nome_raca', 'id_especie']