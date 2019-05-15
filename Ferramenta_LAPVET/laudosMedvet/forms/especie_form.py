from django.forms import ModelForm
from laudosMedvet.models import EspecieModel


class EspecieForm(ModelForm):
    class Meta():
        model = EspecieModel
        fields = ['nome_especie']
