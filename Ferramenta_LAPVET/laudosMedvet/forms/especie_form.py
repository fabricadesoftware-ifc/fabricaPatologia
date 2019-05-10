from django.forms import ModelForm
from django import forms
from laudosMedvet.models import EspecieModel


class EspecieForm(ModelForm):
    class Meta:
        model = EspecieModel
        fields = ['nome_especie']
