from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404

from laudosMedvet.models import EspecieModel
from laudosMedvet.models import RacaModel
from laudosMedvet.models import LaudoModel
from laudosMedvet.models import ImagensModel

from laudosMedvet.models import EstadoModel
from laudosMedvet.models import CidadeModel, RuaModel, BairroModel
from django.db.models import Q


@login_required
def lista_laudos(request):

    # busca uma lista de objetos no BD para usar na consulta
    estados = EstadoModel.objects.all()
    especies = EspecieModel.objects.all()
    lista_raca = RacaModel.objects.all()
    lista_cidade = CidadeModel.objects.all()
    por_bairro = BairroModel.objects.all()
    por_rua = RuaModel.objects.all()
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
    por_cidade = request.GET.get('por_cidade', None)
    por_estado = request.GET.get('por_estado', None)
    por_especie = request.GET.get('por_especie', None)
    por_sistema = request.GET.get('por_sistema', None)
    data_min = request.GET.get('data_min', None)
    data_max = request.GET.get('data_max', None)

    # d_min = datetime.strptime(data_min, "%Y-%m-%d")
    # d_max = datetime.strptime(data_max, "%Y-%m-%d")

    #hoje = date.today().strftime('%Y-%m-%d')

    filtro = Q()

    if por_sistema:
        filtro.add(Q(sistemas__contains=por_sistema), Q.OR)

    if por_especie:
        filtro.add(Q(id_requisicao__cod_animail__id_especie__nome_especie__contains=por_especie), Q.OR)

    if por_raca:
         filtro.add(Q(id_requisicao__cod_animail__raca__nome_raca__contains=por_raca), Q.OR)

    if por_estado:
        filtro.add(Q(id_requisicao__cod_animail__id_estado__nome_estado__contains=por_estado), Q.OR)

    if por_cidade:
        filtro.add(Q(id_requisicao__cod_animail__cidade__nome_cidade__contains=por_cidade), Q.OR)

    if por_bairro:
        filtro.add(Q(id_requisicao__cod_animail__bairro__nome_bairro__contains=por_cidade), Q.OR)

    if por_rua:
        filtro.add(Q(id_requisicao__cod_animail__rua__nome_rua__contains=por_rua), Q.OR)

    # if d_min: #FIXME: resolver o problema do formato das datas
    #     filtro.add(Q(dt_laudo__gte=d_min), Q.OR)
    #
    # if d_max:
    #     filtro.add(Q(dt_laudo__lte=d_max), Q.OR)

    laudos = LaudoModel.objects.filter(filtro)

    #TODO: gráficos com os casos..

    #print(LaudoModel.objects.dates().filter(id=2))
    paginator = Paginator(laudos, 10)
    page = request.GET.get('page')
    list_laudos = paginator.get_page(page)



    return render(request, 'pagina_filtro_laudos.html', {'laudos': list_laudos, 'lista_sistemas':lista_sistemas,
                                                        'especies':especies, 'lista_raca': lista_raca,
                                                         'estados':estados, 'lista_cidade':lista_cidade,
                                                         'por_rua':por_rua, 'por_bairro':por_bairro})

@login_required
def gera_pdf(request, id):
    laudo = get_object_or_404(LaudoModel, pk=id)
    imagens = ImagensModel.objects.all().filter(id_laudo=id)

    return render(request, 'gerar_pdf_filtro.html', {'laudo': laudo, 'imagens':imagens})




