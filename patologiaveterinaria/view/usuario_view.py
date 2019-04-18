from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect
from django.views import View

from patologiaveterinaria.form import UsuarioForm
from patologiaveterinaria.model import UsuarioModel


class CadastroUsuarioView(View):
    template = 'cadastro_usuario.html'

    def get(self,request):
        form = UsuarioForm()
        return render(request, self.template, {'form': form})

    def post(self, request):
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            usuario = UsuarioModel.objects.latest('id')
            usuario.groups.add(Group.objects.get(pk=1))
            usuario.save()
            return redirect('login_user')
        return render(request, self.template, {'form': form})

class LoginView(View):
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is None or not user.is_active:
            return redirect('login_user')
        login(request, user)
        return redirect('principal')

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login_user')
