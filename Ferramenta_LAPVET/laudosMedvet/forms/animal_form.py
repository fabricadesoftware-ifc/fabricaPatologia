

from django.forms import ModelForm
from django import forms
from laudosMedvet.models import AnimalModel
from laudosMedvet.models import ProprietarioModel


class AnimalForm(ModelForm):
    DATA_SEXO = (('Fêmea', 'Fêmea'), ('Macho', 'Macho'))
    sexo = forms.ChoiceField(
        choices=DATA_SEXO,
        widget=forms.RadioSelect(attrs={
            'class': 'radio',
            'id': 'sexo'
        }),
    )

    class Meta():
        model = AnimalModel
        fields = ['nome', 'idade', 'raca', 'sexo', 'cor_pelagem', 'proprietario',
                  'veterinario_responsavel', 'rua']