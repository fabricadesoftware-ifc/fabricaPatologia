# coding=utf-8
from django.forms import ModelForm
from ..models import EstadoModel


class EstadoForm(ModelForm):
    class Meta():
        model = EstadoModel
        fields = ['nome_estado']