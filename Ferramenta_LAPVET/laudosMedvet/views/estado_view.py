from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from laudosMedvet.models import EstadoModel
from laudosMedvet.forms import EstadoForm

@login_required
def index_estado(request):
    estados = EstadoModel.objects.all()
    return render(request, 'enderecos/estado_list.html', {'estados':estados})

@login_required
def new_estado(request):
    form = EstadoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('index_estado')
    return render(request, 'enderecos/estado_new.html', {'form':form})

@login_required
def update_estado(request, id):
    estado = get_object_or_404(EstadoModel, pk=id)
    form = EstadoForm(request.POST or None, request.FILES or None, instance=estado)

    if form.is_valid():
        form.save()
        return redirect('index_estado')
    return render(request, 'enderecos/estado_new.html', {'form':form})


@login_required
def delete_estado(request, id):
    estado = get_object_or_404(EstadoModel, pk=id)
    if request.method == 'POST':
        estado.delete()
        return redirect('index_estado')
    return render(request, 'enderecos/estado_delete.html', {'form':estado})

