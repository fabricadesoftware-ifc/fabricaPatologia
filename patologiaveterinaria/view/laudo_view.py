from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View

from patologiaveterinaria.form import LaudoForm
from patologiaveterinaria.model import LaudoModel

class CadastrarLaudo(View):
    template = 'cadastrar_laudo.html'

    def get(self, request):
        form = LaudoForm
        if not request.user.is_authenticated:
            return HttpResponseRedirect('/')
        return render(request, self.template, {'form': form})

    def post(self, request):
        form = LaudoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('principal')
        return render(request, self.template, {'form': form})
