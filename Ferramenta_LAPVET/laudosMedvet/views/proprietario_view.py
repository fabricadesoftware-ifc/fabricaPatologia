from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from laudosMedvet.forms import ProprietarioForm
from laudosMedvet.models import ProprietarioModel



@login_required
def index_proprietario(request):
    proprietarios = ProprietarioModel.objects.all()
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
    especie = get_object_or_404(ProprietarioModel, pk=id)
    form = ProprietarioForm(request.POST or None, request.FILES or None, instance=especie)

    if form.is_valid():
        form.save()
        return redirect('index_proprietario')
    return render(request, 'pessoas/proprietario_new.html', {'form':form})

@login_required
def delete_proprietario(request, id):
    especie = get_object_or_404(ProprietarioModel, pk=id)
    if request.method == 'POST':
        especie.delete()
        return redirect('index_proprietario')
    return render(request, 'pessoas/proprietario_delete.html')