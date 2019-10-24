from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View
from laudosMedvet.models import UsuarioModel



class PaginaPrincipal(View):
    template = 'principal.html'

    def get(self, request):
        if not request.user.is_authenticated:
            return HttpResponseRedirect('/')
        return render(request, self.template)
