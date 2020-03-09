# coding:utf-8
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from ..models import RequisicaoLaudoModel
from ..forms import RequisicaoLaudoForm


@login_required
def index_requisicao(request):
    tipo = request.GET.get('tipo', None)
    animal = request.GET.get('animal', None)
    nome = request.GET.get('cod_animal', None)
    if tipo is not None:
        requisicoes = RequisicaoLaudoModel.objects.filter(tipo_de_laudo__tipo_laudo__icontains=tipo)
    elif animal is not None:
        requisicoes = RequisicaoLaudoModel.objects.filter(cod_animail__nome__icontains=animal)
    elif nome is not None:
        requisicoes = RequisicaoLaudoModel.objects.filter(cod_animail__proprietario__nome_proprietario__icontains=nome)
    else:
        requisicoes = RequisicaoLaudoModel.objects.all()
    return render(request, 'laudo/requisicao_list.html', {'requisicoes':requisicoes})

@login_required
def new_requisicao(request):
    form = RequisicaoLaudoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('index_requisicao')
    return render(request, 'laudo/requisicao_new.html', {'form':form})

@login_required
def update_requisicao(request, id):
    requisicao = get_object_or_404(RequisicaoLaudoModel, pk=id)
    form = RequisicaoLaudoForm(request.POST or None, request.FILES or None, instance=requisicao)

    if form.is_valid():
        form.save()
        return redirect('index_requisicao')
    return render(request, 'laudo/requisicao_new.html', {'form':form})

@login_required
def delete_requisicao(request, id):
    requisicao = get_object_or_404(RequisicaoLaudoModel, pk=id)
    if request.method == 'POST':
        requisicao.delete()
        return redirect('index_requisicao')
    return render(request, 'laudo/requisicao_delete.html', {'form':requisicao})