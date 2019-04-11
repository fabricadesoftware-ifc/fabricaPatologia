from django import forms
from django.forms import ModelForm

from patologiaveterinaria.model import PatologistaModel

class PatologistaForm(ModelForm):
    nome = forms.CharField(max_length=130)

    class Meta:
        model = PatologistaModel
        exclude = ()