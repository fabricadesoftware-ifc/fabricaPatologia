
from django.forms import ModelForm
from django import forms

from patologiaveterinaria.model import AnimalModel
from patologiaveterinaria.model import CidadeModel
from patologiaveterinaria.model import EstadoModel

class AnimalForm(ModelForm):
    cidades = CidadeModel.objects.all()
    estados = EstadoModel.objects.all()
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
    cidade = forms.ModelChoiceField(required=False,
                                    empty_label="Selecione uma cidade",
                                    queryset=cidades,
                                    widget=forms.Select(attrs={"class": "ui fluid search selection dropdown"})
                                  )
    estado = forms.ModelChoiceField(required=False,
                                    empty_label="Selecione um estado",
                                    queryset=estados,
                                    widget=forms.Select(attrs={"onchange": "get_cidade_natural()",
                                                               "class": "ui fluid search selection dropdown"})
                                    )
    bairro = forms.CharField(max_length=128)
    cep = forms.CharField(max_length=9)


    def save(self, commit=True):
        laudo = super(AnimalForm, self).save(commit=False)
        if commit:
            laudo.save()

    class Meta:
        model = AnimalModel
        exclude = ()
