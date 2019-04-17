from django.forms import ModelForm
from django import forms

from patologiaveterinaria.model import LaudoModel

class LaudoForm(ModelForm):
    historico_clinico = forms.CharField(widget=forms.Textarea)
    descricao_macroscopica = forms.CharField(widget=forms.Textarea)
    descricao_microscopica = forms.CharField(widget=forms.Textarea)
    diagnostico_morfologico = forms.CharField(widget=forms.Textarea)
    comentarios = forms.CharField(widget=forms.Textarea)

    def save(self, commit=True):
        laudo = super(self).save(commit=False)
        if commit:
            laudo.save()

    class Meta:
        model = LaudoModel
        exclude = ()
