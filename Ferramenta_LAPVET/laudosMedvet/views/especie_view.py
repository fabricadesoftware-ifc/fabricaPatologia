# coding:utf-8
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from laudosMedvet.models import EspecieModel
from laudosMedvet.forms import EspecieForm


@login_required
def index_especie(request):
    especies = EspecieModel.objects.all()
    return render(request, 'especie/especie_list.html', {'especies':especies})

@login_required
def new_especie(request):
    form = EspecieForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('index_especie')
    return render(request, 'especie/especie_save.html', {'form':form})

@login_required
def update_especie(request, id):
    especie = get_object_or_404(EspecieModel, pk=id)
    form = EspecieForm(request.POST or None, request.FILES or None, instance=especie)

    if form.is_valid():
        form.save()
        return redirect('index_especie')
    return render(request, 'especie/especie_save.html', {'form':form})


@login_required
def delete_especie(request, id):
    especie = get_object_or_404(EspecieModel, pk=id)
    if request.method == 'POST':
        especie.delete()
        return redirect('index_especie')
    return render(request, 'especie/especie_delete.html')
