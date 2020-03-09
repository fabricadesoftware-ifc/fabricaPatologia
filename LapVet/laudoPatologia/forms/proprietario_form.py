from django.forms import ModelForm

from ..models import ProprietarioModel

class ProprietarioForm(ModelForm):
    class Meta():
        model = ProprietarioModel
        fields = [
            'nome_proprietario',
            'data_nasc',
            'cpf',
            'rg',
            'telefone',
            'celular',
            'email',
            'endereco',
            'numero',
            'complemento',
        ]