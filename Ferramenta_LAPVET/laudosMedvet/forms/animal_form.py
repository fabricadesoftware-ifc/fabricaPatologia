from django.forms import ModelForm
from django.forms import forms
from laudosMedvet.models import AnimalModel


class AnimalForm(ModelForm):

    class Meta():
        model = AnimalModel
        fields = ['nome', 'data_nasc', 'raca','sexo', 'cor_pelagem', 'especie', 'proprietario',
                  'veterinario_responsavel', 'rua']