from django import forms
from django.contrib.auth.models import Group, Permission


class GrupoForm(forms.Form):
    nome_grupo = forms.CharField(max_length=50)