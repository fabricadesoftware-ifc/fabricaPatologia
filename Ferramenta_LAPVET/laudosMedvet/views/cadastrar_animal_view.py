from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View

class AnimalView(View):

    template = 'cadastrar_animal.html'

    def get(self, request):

        if not request.user.is_authenticated:
            return HttpResponseRedirect('login_user')
        return render(request, self.template)
