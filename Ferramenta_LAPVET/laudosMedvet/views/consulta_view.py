# coding:utf-8
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from laudosMedvet.models import RequisicaoLaudoModel, LaudoModel, ImagensModel, EspecieModel, RacaModel

# Consulta por requisições, laudos e imagens


@login_required
def consulta_requisicao(request):
    por_proprietario = request.GET.get('por_proprietario', None)
    por_animal = request.GET.get('por_animal', None)
    por_tipo = request.GET.get('por_tipo', None)

    if por_animal is not None:
        requisicoes = RequisicaoLaudoModel.objects.filter(
            cod_animail__nome__icontains=por_animal
        )
    elif por_proprietario is not None:
        requisicoes = RequisicaoLaudoModel.objects.filter(
            cod_animail__proprietario__nome_proprietario__icontains=por_proprietario
        )
    elif por_tipo is not None:
        requisicoes = RequisicaoLaudoModel.objects.filter(
            tipo_de_laudo__tipo_laudo__icontains=por_tipo
        )
    else:
        requisicoes = RequisicaoLaudoModel.objects.all()
    return render(request, 'consultas/por_requisição.html', {'requisicoes':requisicoes})


@login_required
def visualizar_requisicao(request, id):
    requisicao = get_object_or_404(RequisicaoLaudoModel, pk=id)
    return render(request, 'consultas/requisicao.html', {'requisicao': requisicao})


@login_required
def consulta_laudo(request):

    # busca uma lista de objetos no BD para usar na consulta
    especies = EspecieModel.objects.all()
    lista_raca = RacaModel.objects.all()
    lista_sistemas = ['Cardiovascular',
                      'Pulmonar',
                      'Digestivo',
                      'Endócrino',
                      'Nervoso',
                      'Reprodutivo',
                      'Muscular',
                      'Esquelético',
                      'Tegumentar',
                      'Excretor']

    por_raca = request.GET.get('por_raca', None)
    por_especie = request.GET.get('por_especie', None)
    por_sistema = request.GET.get('por_sistema', None)


    if por_raca is not None:
        laudos = LaudoModel.objects.filter(
            id_requisicao__cod_animail__raca__nome_raca__icontains=por_raca
        )
    elif por_sistema is not None:
        laudos = LaudoModel.objects.filter(
            sistemas__icontains=por_sistema
        )
    elif por_especie is not None:
        laudos = LaudoModel.objects.filter(
            id_requisicao__cod_animail__raca__id_especie__nome_especie__icontains=por_especie
        )
    else:
        laudos = LaudoModel.objects.all()
    return render(request, 'consultas/por_laudo.html', {'laudos': laudos, 'lista_sistemas':lista_sistemas,
                                                        'especies':especies, 'lista_raca': lista_raca})


@login_required
def visualizar_laudo(request, id):
    laudo = get_object_or_404(LaudoModel, pk=id)
    return render(request, 'consultas/laudo.html', {'laudo': laudo})


@login_required
def visualizar_imagens_por_laudo(request, id):
    imagens = ImagensModel.objects.all().filter(id_laudo=id)
    paginator = Paginator(imagens, 1)
    page = request.GET.get('page')
    imagem = paginator.get_page(page)
    return render(request, 'consultas/imagens_laudo.html', {'imagem':imagem})
