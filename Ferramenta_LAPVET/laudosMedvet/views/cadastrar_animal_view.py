from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View

from laudosMedvet.forms import CadastrarAnimalForm

class CadastrarAnimalView(View):

    template = 'cadastrar_animal.html'

    def get(self, request):
        form = CadastrarAnimalForm
        if not request.user.is_authenticated:
            return HttpResponseRedirect('login_user')
        return render(request, self.template, {'form': form})

    def post(self, request):
        form = CadastrarAnimalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('principal')
        return render(request, self.template, {'form': form})