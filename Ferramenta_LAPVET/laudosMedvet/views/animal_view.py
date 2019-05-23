# coding:utf-8
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from laudosMedvet.models import AnimalModel
from laudosMedvet.forms import AnimalForm


@login_required
def index_animal(request):
    nome = request.GET.get('nome', None)
    if nome is not None:
        animais = AnimalModel.objects.filter(nome__icontains=nome)
    else:
        animais = AnimalModel.objects.order_by('nome')
    return render(request, 'animal/animal_list.html', {'animais':animais})

@login_required
def new_animal(request):
    form = AnimalForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('index_animal')
    return render(request, 'animal/animal_new.html', {'form':form})

@login_required
def update_animal(request, id):
    animal = get_object_or_404(AnimalModel, pk=id)
    form = AnimalForm(request.POST or None, request.FILES or None, instance=animal)

    if form.is_valid():
        form.save()
        return redirect('index_animal')
    return render(request, 'animal/animal_new.html', {'form':form})

@login_required
def delete_animal(request, id):
    animal = get_object_or_404(AnimalModel, pk=id)
    if request.method == 'POST':
        animal.delete()
        return redirect('index_animal')
    return render(request, 'animal/animal_delete.html', {'form':animal})