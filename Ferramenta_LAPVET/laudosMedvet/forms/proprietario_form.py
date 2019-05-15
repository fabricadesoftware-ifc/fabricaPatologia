from django.forms import ModelForm

from laudosMedvet.models import ProprietarioModel

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
            'rua',
            'numero',
            'complemento',
        ]