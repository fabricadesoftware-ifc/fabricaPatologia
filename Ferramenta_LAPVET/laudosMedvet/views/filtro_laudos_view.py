from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404

from laudosMedvet.models import EspecieModel
from laudosMedvet.models import RacaModel
from laudosMedvet.models import LaudoModel
from laudosMedvet.models import ImagensModel

from laudosMedvet.models import EstadoModel
from laudosMedvet.models import CidadeModel, RuaModel, BairroModel
from datetime import date
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


    # por_raca = request.GET.get('por_raca', None)
    # por_cidade = request.GET.get('por_cidade', None)
    # por_estado = request.GET.get('por_estado', None)
    # por_especie = request.GET.get('por_especie', None)
    # por_sistema = request.GET.get('por_sistema', None)
    # data_min = request.GET.get('data_min', None)
    # #d_min = datetime.strptime(data_min, "%Y-%m-%d")
    # data_max = request.GET.get('data_max', None)
    # hoje = date.today().strftime('%Y-%m-%d')
    # #d_max = datetime.strptime(data_max, "%Y-%m-%d")

    # if por_sistema is not None:
    #     laudos = LaudoModel.objects.filter(Q(sistemas__contains=por_sistema))
    #
    # elif por_especie is not None:
    #     laudos = LaudoModel.objects.filter(Q(id_requisicao__cod_animail__id_especie__nome_especie__contains=por_especie))
    #
    # elif por_estado is not None: #FIXME: não esta funcionando
    #     laudos = LaudoModel.objects.filter(Q(id_requisicao__cod_animail__id_estado__nome_estado=por_estado))
    #
    # elif data_min or data_max: #TODO: filtrar por data de início e data final
    #     laudos = LaudoModel.objects.filter(Q(dt_laudo__gte=data_min, dt_laudo__lte=data_max))
    #
    # elif por_raca is not None:
    #     laudos = LaudoModel.objects.filter(id_requisicao__cod_animail__raca__nome_raca__contains=por_raca)
    #
    # elif por_cidade is not None:
    #     laudos = LaudoModel.objects.filter(id_requisicao__cod_animail__id_cidade__nome_cidade=por_cidade)
    #
    # elif por_bairro is not None:
    #     laudos = LaudoModel.objects.filter(id_requisicao__cod_animail__rua__id_bairro__nome_bairro=por_cidade)
    #
    # elif por_rua is not None:
    #     laudos = LaudoModel.objects.filter(id_requisicao__cod_animail__rua__nome_rua=por_rua)
    #
    # elif data_min is not None: #TODO: filtrar por data de início e data final
    #     laudos = LaudoModel.objects.filter(dt_laudo__gte=data_min, dt_laudo__lte=data_max)

    procura = request.GET.get('procura', None)

    if procura is not None:
        laudos = LaudoModel.objects.filter(sistemas__contains=procura)| \
                 LaudoModel.objects.filter(id_requisicao__cod_animail__id_especie__nome_especie__contains=procura)

    else:
        laudos = LaudoModel.objects.all()

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




