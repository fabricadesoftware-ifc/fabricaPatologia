# coding:utf-8
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from laudosMedvet.models import RegiaoEstadoModel
from laudosMedvet.forms import RegiaoEstadoForm


@login_required
def index_regiao_est(request):
    regioes = RegiaoEstadoModel.objects.all()
    return render(request, 'enderecos/regiao_estado_list.html', {'regioes':regioes})

@login_required
def new_regiao_est(request):
    form = RegiaoEstadoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('index_regiao_est')
    return render(request, 'enderecos/regiao_estado_new.html', {'form':form})

@login_required
def update_regiao_est(request, id):
    regiao = get_object_or_404(RegiaoEstadoModel, pk=id)
    form = RegiaoEstadoForm(request.POST or None, request.FILES or None, instance=regiao)

    if form.is_valid():
        form.save()
        return redirect('index_regiao_est')
    return render(request, 'enderecos/regiao_estado_new.html', {'form':form})

@login_required
def delete_regiao_est(request, id):
    regiao = get_object_or_404(RegiaoEstadoModel, pk=id)
    if request.method == 'POST':
        regiao.delete()
        return redirect('index_regiao_est')
    return render(request, 'enderecos/regiao_estado_delete.html', {'form':regiao})