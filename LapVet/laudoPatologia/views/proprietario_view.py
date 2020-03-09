from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from ..forms import ProprietarioForm
from ..models import ProprietarioModel


@login_required
def index_proprietario(request):
    proprietarios = ProprietarioModel.objects.all().order_by('nome_proprietario')
    return render(request, 'pessoas/proprietario_list.html', {'proprietarios':proprietarios})


@login_required
def new_proprietario(request):
    form = ProprietarioForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('index_proprietario')
    return render(request, 'pessoas/proprietario_new.html', {'form':form})


@login_required
def update_proprietario(request, id):
    proprietario = get_object_or_404(ProprietarioModel, pk=id)
    form = ProprietarioForm(request.POST or None, request.FILES or None, instance=proprietario)

    if form.is_valid():
        form.save()
        return redirect('index_proprietario')
    return render(request, 'pessoas/proprietario_new.html', {'form':form})


@login_required
def delete_proprietario(request, id):
    proprietario = get_object_or_404(ProprietarioModel, pk=id)
    if request.method == 'POST':
        proprietario.delete()
        return redirect('index_proprietario')
    return render(request, 'pessoas/proprietario_delete.html', {'form':proprietario})