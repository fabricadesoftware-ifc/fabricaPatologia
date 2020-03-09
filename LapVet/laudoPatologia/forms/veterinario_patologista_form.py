from django.forms import ModelForm

from ..models import VeterinarioPatologistaModel


class VeterinarioPatologistaForm(ModelForm):
    class Meta():
        model = VeterinarioPatologistaModel
        fields = ['nome_veterinario_patologista', 'formacao', 'crmv']