from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View

from patologiaveterinaria.model import AnimalModel

class PaginaPrincipal(View):
    template = 'principal.html'

    def get(self, request):
        if not request.user.is_authenticated:
            return HttpResponseRedirect('/')
        return render(request, self.template)


class MostraAnimal(View):
    template = 'mostra_animal.html'

    def get(self, request):
        mostra_animal = AnimalModel.objects.all()
        objeto = {
            'mostra_animal': mostra_animal
        }
        if not request.user.is_authenticated:
            return HttpResponseRedirect('/')
        return render(request, self.template, objeto)