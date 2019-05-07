from django.forms import ModelForm
from django import forms

from laudosMedvet.models import CadastrarAnimalModel

class CadastrarAnimalForm(ModelForm):

    sexo = forms.ChoiceField(widget=forms.RadioSelect, choices=CadastrarAnimalModel.sexo)

    class Meta:
        model = CadastrarAnimalModel
        fields = ['nome', 'raca', 'especie', 'proprietario', 'telefone_proprietario',
                  'veterinario_responsavel', 'telefone_veterinario_responsavel']