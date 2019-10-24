from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group, User
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View

from laudosMedvet.forms import UsuarioForm, UserForm, FormMudarSenha
from laudosMedvet.models import UsuarioModel, UserModel



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

# class CadastroAcesso(View):
#     template = 'cadastro_usuario.html'
#
#     def get(self,request):
#         form = UserForm()
#         return render(request, self.template, {'form': form})
#
#     def post(self, request):
#         form = UserForm(request.POST)
#         if form.is_valid():
#             form.save()
#             usuario = UsuarioModel.objects.last()
#             if Group.objects.all().count() >= 1:
#                 usuario.groups.add(Group.objects.last())
#                 usuario.save()
#                 return redirect('login_user')
#             else:
#                 usuario.save()
#                 return redirect('login_user')
#         return render(request, self.template, {'form': form})

class LoginView(View):
    def post(self, request):
        grupos = Group.objects.all()
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is None or not user.is_active:
            return redirect('login_user')
        else:
            login(request, user)
            if grupos.count() < 1:
                return redirect('new_grupo')
            return redirect('principal')

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login_user')


@login_required
def index_user(request, id):
    users = get_object_or_404(UserModel, pk=id)
    perfil = UsuarioModel.objects.all()
    return render(request, 'pessoas/perfil_user.html', {'users':users})


@login_required
def new_perfil_user(request):
    form = UsuarioForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        user = form.save(commit=False)
        user.username = request.user
        user.save()
        return redirect('index_user')
    return render(request, 'pessoas/perfil_user_edit.html', {'form':form})

# @login_required
# def delete_user(request, id):
#     user = get_object_or_404(UsuarioModel, pk=id)
#     if request.method == 'POST':
#         user.delete()
#         return redirect('index_user')
#     return render(request, 'pessoas/user_delete.html', {'form':user})

# @login_required
# def update_user(request, id):
#     user = get_object_or_404(UsuarioModel, pk=id)
#     form = UsuarioForm(request.POST or None, request.FILES or None, instance=user)
#
#     if form.is_valid():
#         form.save()
#         return redirect('index_user')
#     return render(request, 'pessoas/perfil_user_edit.html', {'form':form})


def update_password(request, user_id):
    usuario_django = User.objects.get(pk=user_id)

    if request.method == 'POST':

        form = FormMudarSenha(request.POST)

        if form.is_valid():
            usuario_django.set_password(request.POST['nova_senha'])
            usuario_django.save()

            return redirect('/home/')

    else:
        form = FormMudarSenha()

    return render(request, 'pessoas/mudar_senha.html', {
        'form': form,
        'usuario_id': usuario_django.id
    })

