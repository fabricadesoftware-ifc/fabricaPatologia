from django import forms
from django.forms import ModelForm

from patologiaveterinaria.model import ProprietarioModel

class ProprietarioForm(ModelForm):
    nome = forms.CharField(max_length=130)
    telefone = forms.CharField(max_length=20, blank=True)
    endereco = forms.CharField(max_length=128, blank=True)

    class Meta:
        model = ProprietarioModel
        exclude = ()