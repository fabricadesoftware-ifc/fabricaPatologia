# coding:utf-8
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from laudosMedvet.models import LaudoModel
from laudosMedvet.forms import LaudoForm


@login_required
def index_laudo(request):
    requisicao = request.GET.get('requisicao', None)
    tipo = request.GET.get('tipo', None)
    animal = request.GET.get('animal', None)
    if requisicao is not None:
        laudos = LaudoModel.objects.filter(id_requisicao__id__icontains=requisicao)
    elif tipo is not None:
        laudos = LaudoModel.objects.filter(id_requisicao__tipo_de_laudo__tipo_laudo__icontains=tipo)
    elif animal is not None:
        laudos = LaudoModel.objects.filter(id_requisicao__cod_animail__id__icontains=animal)
    else:
        laudos = LaudoModel.objects.all()
    return render(request, 'laudo/laudo_list.html', {'laudos':laudos})

@login_required
def new_laudo(request):
    form = LaudoForm(request.POST or None, request.FILES or None)
    if form.is_valid(): # TODO: fazer com que apareça apenas os ids das requisições que não tem laudo!!
        form.save()
        return redirect('index_laudo')
    return render(request, 'laudo/laudo_new.html', {'form':form})

@login_required
def update_laudo(request, id):
    laudo = get_object_or_404(LaudoModel, pk=id)
    form = LaudoForm(request.POST or None, request.FILES or None, instance=laudo)

    if form.is_valid():
        form.save()
        return redirect('index_laudo')
    return render(request, 'laudo/laudo_new.html', {'form':form})


@login_required
def delete_laudo(request, id):
    laudo = get_object_or_404(LaudoModel, pk=id)
    if request.method == 'POST':
        laudo.delete()
        return redirect('index_laudo')
    return render(request, 'laudo/laudo_delete.html', {'form':laudo})