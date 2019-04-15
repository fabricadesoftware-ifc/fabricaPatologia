from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View
from patologiaveterinaria.form.laudo_form import LaudoForm

class CadastrarLaudo(View):
    template = 'cadastrar_laudo.html'

    def get(self, request):
        return render(request, self.template)

    def post(self, request):
        form = LaudoForm
        if form.is_valid():
            form.save()
            return redirect('principal')
        return render(request, self.template, {'form': form})