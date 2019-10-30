from django.forms import ModelForm

from laudosMedvet.models import VeterinarioPatologistaModel

class VeterinarioPatologistaForm(ModelForm):
    class Meta():
        model = VeterinarioPatologistaModel
        fields = ['nome', 'formacao', 'crmv']