from django.forms import ModelForm

from laudosMedvet.models import VeterinarioresponsavelModel

class VeterinarioResponsavelForm(ModelForm):
    class Meta():
        model = VeterinarioresponsavelModel
        fields = ['nome_veterinario', 'telefone', 'crmv']