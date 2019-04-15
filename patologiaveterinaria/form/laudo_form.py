from django.forms import ModelForm
from django import forms

from patologiaveterinaria.model import LaudoModel


class LaudoForm(ModelForm):
    nome = forms.CharField(max_length=130)
    idade = forms.CharField(max_length=2)
    especie = forms.CharField(max_length=100)

    def save(self, commit=True):
        produto = super(self).save(commit=False)
        if commit:
            produto.save()


    class Meta:
        model = LaudoModel
        exclude = ()
