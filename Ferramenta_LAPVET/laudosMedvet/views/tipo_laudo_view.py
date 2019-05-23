# coding:utf-8
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from laudosMedvet.models import TipoLaudoModel
from laudosMedvet.forms import TipoLaudoForm


@login_required
def index_tipo_laudo(request):
    tipos = TipoLaudoModel.objects.all()
    return render(request, 'laudo/tipo_laudo_list.html', {'tipos':tipos})

@login_required
def new_tipo_laudo(request):
    form = TipoLaudoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('index_tipo_laudo')
    return render(request, 'laudo/tipo_laudo_new.html', {'form':form})

@login_required
def update_tipo_laudo(request, id):
    tipo = get_object_or_404(TipoLaudoModel, pk=id)
    form = TipoLaudoForm(request.POST or None, request.FILES or None, instance=tipo)

    if form.is_valid():
        form.save()
        return redirect('index_tipo_laudo')
    return render(request, 'laudo/tipo_laudo_new.html', {'form':form})

@login_required
def delete_tipo_laudo(request, id):
    tipo = get_object_or_404(TipoLaudoModel, pk=id)
    if request.method == 'POST':
        tipo.delete()
        return redirect('index_tipo_laudo')
    return render(request, 'laudo/tipo_laudo_delete.html', {'form':tipo})