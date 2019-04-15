from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View


class CadastrarLaudo(View):
    template = 'cadastrar_laudo.html'

    def get(self, request):
        return render(request, self.template)