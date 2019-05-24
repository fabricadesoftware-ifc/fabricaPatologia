from django.forms import ModelForm
from django import forms
from laudosMedvet.models import AnimalModel


class AnimalForm(ModelForm):
    DATA_SEXO = (('F', 'Fêmea'), ('M', 'Macho'))
    sexo = forms.ChoiceField(
        choices=DATA_SEXO,
        widget=forms.RadioSelect(attrs={
            'class': 'radio',
            'id': 'sexo'
        }),
    )

    class Meta():
        model = AnimalModel
        fields = ['nome', 'data_nasc', 'raca', 'sexo', 'cor_pelagem', 'especie', 'proprietario',
                  'veterinario_responsavel', 'rua']