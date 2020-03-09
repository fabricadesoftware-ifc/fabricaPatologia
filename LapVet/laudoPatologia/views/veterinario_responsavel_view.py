# coding:utf-8
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from ..models import VeterinarioResponsavelModel
from ..forms import VeterinarioResponsavelForm


@login_required
def index_vet_resp(request):
    veterinarios = VeterinarioResponsavelModel.objects.all().order_by('nome_veterinario')
    return render(request, 'pessoas/veterinario_resp_list.html', {'veterinarios':veterinarios})


@login_required
def new_vet_resp(request):
    form = VeterinarioResponsavelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('index_vet_resp')
    return render(request, 'pessoas/veterinario_resp_new.html', {'form':form})


@login_required
def update_vet_resp(request, id):
    veterinario = get_object_or_404(VeterinarioResponsavelModel, pk=id)
    form = VeterinarioResponsavelForm(request.POST or None, request.FILES or None, instance=veterinario)
    if form.is_valid():
        form.save()
        return redirect('index_vet_resp')
    return render(request, 'pessoas/veterinario_resp_new.html', {'form':form})


@login_required
def delete_vet_resp(request, id):
    veterinario = get_object_or_404(VeterinarioResponsavelModel, pk=id)
    if request.method == 'POST':
        veterinario.delete()
        return redirect('index_vet_resp')
    return render(request, 'pessoas/veterinario_resp_delete.html', {'form':veterinario})