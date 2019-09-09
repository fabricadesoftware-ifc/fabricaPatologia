# coding:utf-8
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import Group

from laudosMedvet.models import PermissaoModel
from laudosMedvet.forms import GrupoForm


@login_required
def index_grupo(request):
    grupos = Group.objects.all().order_by('name')
    return render(request, 'pessoas/grupos_list.html', {'grupos':grupos})

@login_required
def new_grupo(request):
    form = GrupoForm(request.POST or None, request.FILES or None)
    form_permissions = PermissaoModel.objects.all()
    if form.is_valid() and form_permissions:
        grupo = Group()
        grupo.name = request.POST['nome_grupo']
        grupo.save()
        return redirect('index_grupo')
    return render(request, 'pessoas/grupo_new.html', {'form':form, 'form_permissions':form_permissions})

@login_required
def update_grupo(request, id):
    grupo = get_object_or_404(Group, pk=id)
    form_permissions = PermissaoModel.objects.all()
    form = GrupoForm(request.POST or None, request.FILES or None, grupo)

    if form.is_valid():
        grupo = Group()
        grupo.name = request.POST['nome_grupo']
        form.save()
        return redirect('index_grupo')
    return render(request, 'pessoas/grupo_new.html', {'form':form, 'form_permissions':form_permissions})

@login_required
def delete_grupo(request, id):
    grupo = get_object_or_404(Group, pk=id)
    if request.method == 'POST':
        grupo.delete()
        return redirect('index_grupo')
    return render(request, 'pessoas/grupo_delete.html', {'form':grupo})