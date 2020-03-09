from django.forms import ModelForm
from ..models import EspecieModel


class EspecieForm(ModelForm):
    class Meta():
        model = EspecieModel
        fields = ['nome_especie']
