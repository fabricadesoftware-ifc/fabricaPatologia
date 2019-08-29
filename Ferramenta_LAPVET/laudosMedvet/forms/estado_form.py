from django.forms import ModelForm
from laudosMedvet.models import EstadoModel


class EstadoForm(ModelForm):
    class Meta():
        model = EstadoModel
        fields = ['nome_estado']