# coding:utf-8
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from laudosMedvet.models import RuaModel
from laudosMedvet.forms import RuaForm


@login_required
def index_rua(request):
    ruas = RuaModel.objects.all().order_by('nome_rua')
    return render(request, 'enderecos/rua_list.html', {'ruas':ruas})

@login_required
def new_rua(request):
    form = RuaForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('index_rua')
    return render(request, 'enderecos/rua_new.html', {'form':form})

@login_required
def update_rua(request, id):
    rua = get_object_or_404(RuaModel, pk=id)
    form = RuaForm(request.POST or None, request.FILES or None, instance=rua)

    if form.is_valid():
        form.save()
        return redirect('index_rua')
    return render(request, 'enderecos/rua_new.html', {'form':form})

@login_required
def delete_rua(request, id):
    rua = get_object_or_404(RuaModel, pk=id)
    if request.method == 'POST':
        rua.delete()
        return redirect('index_rua')
    return render(request, 'enderecos/rua_delete.html', {'form':rua})