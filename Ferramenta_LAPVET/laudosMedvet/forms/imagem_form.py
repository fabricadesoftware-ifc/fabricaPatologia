from django.forms import ModelForm
from laudosMedvet.models import ImagensModel


class ImagemForm(ModelForm):
    class Meta():
        model = ImagensModel
        fields = ['nome_imagem', 'imagem', 'id_laudo']