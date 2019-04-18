from django.forms import ModelForm
from django import forms

from patologiaveterinaria.model import LaudoModel
from patologiaveterinaria.model import TipoLaudoModel

class LaudoForm(ModelForm):
    tipo = forms.ChoiceField(widget=forms.Select, choices=TipoLaudoModel.tipo)
    historico_clinico = forms.CharField(widget=forms.Textarea)
    descricao_macroscopica = forms.CharField(widget=forms.Textarea)
    descricao_microscopica = forms.CharField(widget=forms.Textarea)
    diagnostico_morfologico = forms.CharField(widget=forms.Textarea)
    comentarios = forms.CharField(widget=forms.Textarea)

    def save(self, commit=True):
        laudo = super(LaudoForm, self).save(commit=False)
        if commit:
            laudo.save()

    class Meta:
        model = LaudoModel
        exclude = ()
