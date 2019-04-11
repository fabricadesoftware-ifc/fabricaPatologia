from django import forms
from django.forms import ModelForm

from patologiaveterinaria.model import AnimalModel
from patologiaveterinaria.model import EspecieModel

class AnimalForm(ModelForm):
    nome = forms.CharField(max_length=300, null=False)
    especie = forms.ModelChoiceField(required=False,
                                     empty_label="Selecione a espécie",
                                     queryset=EspecieModel.objects.all(),
                                     whidget=forms.Select(attrs={"onchange": "get_especie()",
                                                                 "class": "ui fluid search selection dropdown"})
                                     )

    raca = forms.CharField(max_length=100)
    sex = (('Macho', 'Macho'), ('Femea', 'Femea'))
    sexo = forms.ChoiceField(required=False,
                             widget=forms.RadioSelect,
                             choices=sex,
                             )
    idade = forms.CharField(max_length=30)

    class Meta:
        model = AnimalModel
        exclude = ()