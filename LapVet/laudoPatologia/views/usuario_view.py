from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View

from ..forms import UserForm
from ..models import UserModel


class CadastroPrimeiroAcesso(View):
    template = 'cadastro_usuario.html'

    def get(self,request):
        form = UserForm()
        return render(request, self.template, {'form': form})

    def post(self, request):
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            usuario = UserModel.objects.latest('id')
            usuario.save()
            return redirect('login_user')
        return render(request, self.template, {'form': form})

@login_required
def update_usuario(request, id):
    usuario = get_object_or_404(UserModel, pk=id)
    form = UserForm(request.POST or None, request.FILES or None, instance=usuario)
    if form.is_valid():
        form.save()
        usuario.save()
        return redirect('principal')
    return render(request, 'edit_usuario.html', {'form':form})

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
