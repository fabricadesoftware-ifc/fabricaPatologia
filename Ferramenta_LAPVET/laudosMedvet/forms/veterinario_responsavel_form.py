from django.forms import ModelForm

from laudosMedvet.models import VeterinarioResponsavelModel

class VeterinarioResponsavelForm(ModelForm):
    class Meta():
        model = VeterinarioResponsavelModel
        fields = ['nome_veterinario', 'telefone', 'crmv']