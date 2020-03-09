from django.forms import ModelForm

from ..models import CidadeModel


class CidadeForm(ModelForm):
    class Meta():
        model = CidadeModel
        fields = ['id_estado', 'nome_cidade']