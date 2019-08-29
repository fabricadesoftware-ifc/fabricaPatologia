from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404

from laudosMedvet.models import EspecieModel
from laudosMedvet.models import RacaModel
from laudosMedvet.models import LaudoModel
from laudosMedvet.models import ImagensModel

from laudosMedvet.models import EstadoModel
from laudosMedvet.models import CidadeModel


@login_required
def lista_laudos(request):

    # busca uma lista de objetos no BD para usar na consulta
    por_estado = [
        'Acre', 'Alagoas','Amapá','Amazonas', 'Bahia', 'Ceará' ,
        'Distrito Federal', 'Espírito Santo' , 'Goiás' , 'Maranhão' ,
        'Mato Grosso' , 'Mato Grosso do Sul', 'Minas Gerais' ,
        'Pará' , 'Paraíba', 'Paraná', 'Pernambuco', 'Piauí',
        'Rio de Janeiro', 'Rio Grande do Norte', 'Rio Grande do Sul',
        'Rondônia', 'Roraima', 'Santa Catarina', 'São Paulo', 'Sergipe',
        'Tocantins'
    ]
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
    elif por_estado is not None:
        laudos = LaudoModel.objects.filter(
            id_requisicao__cod_animail__rua__id_bairro__id_cidade__id_estado__nome_estado__icontains=por_estado
        )
    else:
        laudos = LaudoModel.objects.all()

    paginator = Paginator(laudos, 20)
    page = request.GET.get('page')
    list_laudos = paginator.get_page(page)
    return render(request, 'pagina_filtro_laudos.html', {'laudos': list_laudos, 'lista_sistemas':lista_sistemas,
                                                        'especies':especies, 'lista_raca': lista_raca,
                                                         'por_estado':por_estado})