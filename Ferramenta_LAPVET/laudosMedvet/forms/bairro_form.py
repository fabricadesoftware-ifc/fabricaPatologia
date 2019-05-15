from django.forms import ModelForm

from laudosMedvet.models import BairroModel

class BairroForm(ModelForm):
    class Meta():
        model = BairroModel
        fields = ['id_cidade', 'nome_bairro']