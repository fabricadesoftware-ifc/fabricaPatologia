from django.forms import ModelForm
from django import forms

from patologiaveterinaria.model import AnimalModel


class AnimalForm(ModelForm):
    nome = forms.CharField(max_length=130)
    idade = forms.CharField(max_length=2)
    especie = forms.ChoiceField(widget=forms.Select, choices=AnimalModel.especie)
    raca = forms.CharField(max_length=100)
    pelagem = forms.CharField(max_length=130)
    sexo = forms.ChoiceField(widget=forms.RadioSelect, choices=AnimalModel.sexo)
    proprietario = forms.CharField(max_length=130)
    telefone = forms.CharField(max_length=11)
    veterinario_responsavel = forms.CharField(max_length=130)
    telefone_vet = forms.CharField(max_length=11)
    endereco = forms.CharField(max_length=300)

    def save(self, commit=True):
        laudo = super(self).save(commit=False)
        if commit:
            laudo.save()

    class Meta:
        model = AnimalModel
        exclude = ()
