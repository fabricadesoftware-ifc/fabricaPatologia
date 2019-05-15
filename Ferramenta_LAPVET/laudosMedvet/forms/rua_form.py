from django.forms import ModelForm

from laudosMedvet.models import RuaModel

class RuaForm(ModelForm):
    class Meta():
        model = RuaModel
        fields = ['id_bairro', 'nome_rua']