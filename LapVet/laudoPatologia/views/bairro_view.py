# coding:utf-8
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from ..models import BairroModel, CidadeModel, EstadoModel
from ..forms import BairroForm


@login_required
def index_bairro(request):
    procura = request.GET.get('procura', None)
    if procura is not None:
        bairros = BairroModel.objects.filter(nome_bairro__icontains=procura)
    else:
        bairros = BairroModel.objects.all().order_by('nome_bairro')
    return render(request, 'enderecos/bairro_list.html', {'bairros':bairros})

@login_required
def new_bairro(request):
    form = BairroForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('index_bairro')
    return render(request, 'enderecos/bairro_new.html', {'form':form})

@login_required
def update_bairro(request, id):
    bairro = get_object_or_404(BairroModel, pk=id)
    form = BairroForm(request.POST or None, request.FILES or None, instance=bairro)

    if form.is_valid():
        form.save()
        return redirect('index_bairro')
    return render(request, 'enderecos/bairro_new.html', {'form':form})

@login_required
def delete_bairro(request, id):
    bairro = get_object_or_404(BairroModel, pk=id)
    if request.method == 'POST':
        bairro.delete()
        return redirect('index_bairro')
    return render(request, 'enderecos/bairro_delete.html', {'form':bairro})