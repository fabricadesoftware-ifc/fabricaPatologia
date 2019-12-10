from django.forms import ModelForm
from django import forms
from laudosMedvet.models import AnimalModel, RacaModel, CidadeModel, BairroModel, RuaModel


class AnimalForm(ModelForm):
    DATA_SEXO = (('Fêmea', 'Fêmea'), ('Macho', 'Macho'))
    sexo = forms.ChoiceField(
        choices=DATA_SEXO,
        widget=forms.RadioSelect(attrs={
            'class': 'radio',
            'id': 'sexo'}),
    )

    class Meta():
        model = AnimalModel
        fields = ('nome', 'idade', 'id_especie', 'raca', 'sexo', 'cor_pelagem', 'proprietario',
                  'veterinario_responsavel', 'id_estado', 'cidade', 'bairro', 'rua', 'numero', 'complemento')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['raca'].queryset = RacaModel.objects.none()

        if 'id_especie' in self.data:
            try:
                especie_id = int(self.data.get('id_especie'))
                self.fields['raca'].queryset = RacaModel.objects.filter(id_especie_id=especie_id).order_by('nome_raca')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['raca'].queryset = self.instance.id_especie.raca_set.order_by('nome_raca')

        super().__init__(*args, **kwargs)
        self.fields['cidade'].queryset = CidadeModel.objects.none()

        if 'estado' in self.data:
            try:
                estado = int(self.data.get('estado'))
                self.fields['cidade'].queryset = CidadeModel.objects.filter(id_estado_id=estado).order_by('nome_cidade')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['cidade'].queryset = self.instance.id_estado.cidade_set.order_by('nome_cidade')

        super().__init__(*args, **kwargs)
        self.fields['bairro'].queryset = BairroModel.objects.none()

        if 'cidade' in self.data:
            try:
                cidade = int(self.data.get('cidade'))
                self.fields['bairro'].queryset = BairroModel.objects.filter(id_cidade_id=cidade).order_by('nome_bairro')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['bairro'].queryset = self.instance.id_cidade.bairro_set.order_by('nome_bairro')

        super().__init__(*args, **kwargs)
        self.fields['rua'].queryset = RuaModel.objects.none()

        if 'bairro' in self.data:
            try:
                bairro = int(self.data.get('bairro'))
                self.fields['rua'].queryset = RuaModel.objects.filter(id_bairro_id=bairro).order_by('nome_rua')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['rua'].queryset = self.instance.id_bairro.rua_set.order_by('nome_rua')