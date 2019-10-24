# coding:utf-8
from django import forms
from django.core.exceptions import ValidationError


class FormMudarSenha(forms.Form):
    nova_senha = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'span5',
            'id': 'nova_senha',
            'placeholder': 'Digite a sua nova senha...',
        }
        )
    )

    confirmar_senha = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'span5',
            'id': 'confirmar_senha',
            'placeholder': 'Confirmar a sua nova senha...',
        }
        )
    )

    def clean_confirmar_senha(self):

        nova_senha = self.cleaned_data['nova_senha']
        confirmar_senha = self.cleaned_data['confirmar_senha']

        if nova_senha != confirmar_senha:
            raise forms.ValidationError('As senhas não conferem. Digite novamente')

        if len(nova_senha) < 6:
            raise ValidationError('A senha deve ter no mínimo 6 caracteres!')

        return nova_senha


