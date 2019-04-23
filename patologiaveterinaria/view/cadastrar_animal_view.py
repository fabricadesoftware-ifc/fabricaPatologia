from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View
from patologiaveterinaria.form.cadastrar_animal_form import AnimalForm
from patologiaveterinaria.model.laudo_model import LaudoModel

class CadastrarAnimal(View):
    template = 'cadastrar_animal.html'

    def get(self, request):
        form = AnimalForm
        if not request.user.is_authenticated:
            return HttpResponseRedirect('login_user')
        return render(request, self.template, {'form': form})

    def post(self, request):
        form = AnimalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('principal')
        return render(request, self.template, {'form': form})

class MostraLaudos(View):

    def get(self, request):
        lista_laudos = LaudoModel.objects.all()
        objeto = {
            'lista_laudos': lista_laudos
        }

        if not request.user.is_authenticated:
            return HttpResponseRedirect('login_user')
        return render(request, self.template, objeto)