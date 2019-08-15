from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from laudosMedvet.models import EspecieModel
from laudosMedvet.models import RacaModel
from laudosMedvet.models import LaudoModel
from laudosMedvet.models import ImagensModel

@login_required
def lista_laudos(request):

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
    return render(request, 'pagina_filtro_laudos.html', {'laudos': laudos, 'lista_sistemas':lista_sistemas,
                                                        'especies':especies, 'lista_raca': lista_raca})