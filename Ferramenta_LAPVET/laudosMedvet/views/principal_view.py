from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View


class PaginaPrincipal(View):
    template = 'principal.html'

    def get(self, request):
        if not request.user.is_authenticated:
            return HttpResponseRedirect('/')
        return render(request, self.template)


