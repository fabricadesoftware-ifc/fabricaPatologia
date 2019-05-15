from django.forms import ModelForm
from laudosMedvet.models import RegiaoFederalModel

class RegiaoFederalForm(ModelForm):
    class Meta:
        model = RegiaoFederalModel
        fields = ['nome_regiao']