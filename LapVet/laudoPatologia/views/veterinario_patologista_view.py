# coding:utf-8
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from ..models import VeterinarioPatologistaModel
from ..forms import VeterinarioPatologistaForm


@login_required
def index_vet_pat(request):
    veterinarios = VeterinarioPatologistaModel.objects.all().order_by('nome_veterinario_patologista')
    return render(request, 'laudo/veterinario_patologista_list.html', {'veterinarios':veterinarios})

@login_required
def new_vet_pat(request):
    form = VeterinarioPatologistaForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('index_vet_pat')
    return render(request, 'laudo/veterinario_patologista_new.html', {'form':form})

@login_required
def update_vet_pat(request, id):
    veterinario = get_object_or_404(VeterinarioPatologistaModel, pk=id)
    form = VeterinarioPatologistaForm(request.POST or None, request.FILES or None, instance=veterinario)

    if form.is_valid():
        form.save()
        return redirect('index_vet_pat')
    return render(request, 'laudo/veterinario_patologista_new.html', {'form':form})

@login_required
def delete_vet_pat(request, id):
    veterinario = get_object_or_404(VeterinarioPatologistaModel, pk=id)
    if request.method == 'POST':
        veterinario.delete()
        return redirect('index_vet_pat')
    return render(request, 'laudo/veterinario_patologista_delete.html', {'form':veterinario})