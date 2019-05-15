# coding:utf-8
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from laudosMedvet.models import RegiaoFederalModel
from laudosMedvet.forms import RegiaoFederalForm


@login_required
def index_regiao_fed(request):
    regioes = RegiaoFederalModel.objects.all()
    return render(request, 'enderecos/regiao_feredal_list.html', {'regioes':regioes})

@login_required
def new_regiao_fed(request):
    form = RegiaoFederalForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('index_regiao_fed')
    return render(request, 'enderecos/regiao_federal_new.html', {'form':form})

@login_required
def update_regiao_fed(request, id):
    regiao = get_object_or_404(RegiaoFederalModel, pk=id)
    form = RegiaoFederalForm(request.POST or None, request.FILES or None, instance=regiao)

    if form.is_valid():
        form.save()
        return redirect('index_regiao_fed')
    return render(request, 'enderecos/regiao_federal_new.html', {'form':form})

@login_required
def delete_regiao_fed(request, id):
    regiao = get_object_or_404(RegiaoFederalModel, pk=id)
    if request.method == 'POST':
        regiao.delete()
        return redirect('index_regiao_fed')
    return render(request, 'enderecos/regiao_federal_delete.html')