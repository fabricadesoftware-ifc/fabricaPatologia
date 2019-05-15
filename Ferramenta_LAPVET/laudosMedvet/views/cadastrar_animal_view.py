from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View
from laudosMedvet.forms import AnimalForm
from laudosMedvet.models import AnimalModel

class AnimalView(View):
    template = 'animal/cadastrar_animal.html'

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