from django.forms import ModelForm
from django import forms
from laudosMedvet.models import AnimalModel, RacaModel, CidadeModel, BairroModel, RuaModel


class AnimalUpdateForm(ModelForm):
    DATA_SEXO = (('Fêmea', 'Fêmea'), ('Macho', 'Macho'))
    sexo = forms.ChoiceField(
        choices=DATA_SEXO,
        widget=forms.RadioSelect(attrs={
            'class': 'radio',
            'id': 'sexo'}),
    )

    class Meta():
        model = AnimalModel
        fields = ('nome', 'idade', 'id_especie', 'raca', 'sexo', 'cor_pelagem', 'proprietario',
                  'veterinario_responsavel', 'id_estado', 'cidade', 'bairro', 'rua', 'numero', 'complemento')