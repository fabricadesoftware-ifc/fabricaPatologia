from django.forms import ModelForm
from django import forms
from laudosMedvet.models import LaudoModel


class LaudoForm(ModelForm):
    DATA = (('Cardiovascular', 'Cardiovascular'),
            ('Pulmonar', 'Pulmonar'),
            ('Digestivo', 'Digestivo'),
            ('Endócrino', 'Endócrino'),
            ('Nervoso', 'Nervoso'),
            ('Reprodutivo', 'Reprodutivo'),
            ('Muscular', 'Muscular'),
            ('Esquelético', 'Esquelético'),
            ('Tegumentar', 'Tegumentar'),
            ('Excretor', 'Excretor'),
             )
    sistemas = forms.ChoiceField(
        choices=DATA,
        widget=forms.CheckboxSelectMultiple(attrs={
            'class': 'checkbox',
            'id': 'sistemas'
        }),
    )

    class Meta():
        model = LaudoModel
        fields = ['id_requisicao', 'descricao_microscopica', 'diagnostico_morfologico', 'sistemas',
                  'etiologia', 'diagnostico_final', 'comentarios', 'dt_laudo']