# coding:utf-8
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from laudosMedvet.models import ImagensModel
from laudosMedvet.forms import ImagemForm


@login_required
def index_imagem(request):
    imagens = ImagensModel.objects.all()
    return render(request, 'laudo/imagem_list.html', {'imagens':imagens})

@login_required
def new_imagem(request):
    form = ImagemForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('index_imagem')
    return render(request, 'laudo/imagem_new.html', {'form':form})

@login_required
def update_imagem(request, id):
    imagem = get_object_or_404(ImagensModel, pk=id)
    form = ImagemForm(request.POST or None, request.FILES or None, instance=imagem)

    if form.is_valid():
        form.save()
        return redirect('index_imagem')
    return render(request, 'laudo/imagem_new.html', {'form':form})


@login_required
def delete_imagem(request, id):
    imagem = get_object_or_404(ImagensModel, pk=id)
    if request.method == 'POST':
        imagem.delete()
        return redirect('index_imagem')
    return render(request, 'laudo/imagem_delete.html', {'form':imagem})