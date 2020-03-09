from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from ..models import RacaModel
from ..forms import RacaForm


@login_required
def index_raca(request):
    racas = RacaModel.objects.all().order_by('nome_raca')
    return render(request, 'animal/raca_list.html', {'racas':racas})


@login_required
def new_raca(request):
    form = RacaForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('index_raca')
    return render(request, 'animal/raca_new.html', {'form':form})


@login_required
def update_raca(request, id):
    raca = get_object_or_404(RacaModel, pk=id)
    form = RacaForm(request.POST or None, request.FILES or None, instance=raca)

    if form.is_valid():
        form.save()
        return redirect('index_raca')
    return render(request, 'animal/raca_new.html', {'form':form})


@login_required
def delete_raca(request, id):
    raca = get_object_or_404(RacaModel, pk=id)
    if request.method == 'POST':
        raca.delete()
        return redirect('index_raca')
    return render(request, 'animal/raca_delete.html', {'form':raca})