# coding:utf-8
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from laudosMedvet.models import CidadeModel
from laudosMedvet.forms import CidadeForm


@login_required
def index_cidade(request):
    cidades = CidadeModel.objects.all()
    return render(request, 'enderecos/cidade_list.html', {'cidades':cidades})

@login_required
def new_cidade(request):
    form = CidadeForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('index_cidade')
    return render(request, 'enderecos/cidade_new.html', {'form':form})

@login_required
def update_cidade(request, id):
    cidade = get_object_or_404(CidadeModel, pk=id)
    form = CidadeForm(request.POST or None, request.FILES or None, instance=cidade)

    if form.is_valid():
        form.save()
        return redirect('index_cidade')
    return render(request, 'enderecos/cidade_new.html', {'form':form})

@login_required
def delete_cidade(request, id):
    cidade = get_object_or_404(CidadeModel, pk=id)
    if request.method == 'POST':
        cidade.delete()
        return redirect('index_cidade')
    return render(request, 'enderecos/cidade_delete.html')