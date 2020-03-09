from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render

from ..models import EspecieModel
from ..models import RacaModel
from ..models import LaudoModel

from ..forms import AnimalForm

from ..models import EstadoModel
from ..models import (CidadeModel, RuaModel, BairroModel, EspecieModel, RacaModel,
                                 LaudoModel, TipoLaudoModel)
from django.db.models import Q

import folium
import pandas as pd
from folium.plugins import HeatMap


@login_required
def lista_laudos(request):

    tipo_laudo = TipoLaudoModel.objects.all()
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
    por_sistema = request.GET.getlist('por_sistema', None)
    data_min = request.GET.get('data_min', None)
    data_max = request.GET.get('data_max', None)
    etiologia = request.GET.get('etiologia', None)
    por_tipo_laudo = request.GET.get('por_tipo_laudo', None)
    morfologico = request.GET.get('morfologico', None)

    filtro = Q()

    if por_sistema:
        for sis in por_sistema:
            filtro.add(Q(sistemas__contains=sis), Q.AND)

    if etiologia:
        filtro.add(Q(etiologia__icontains=etiologia), Q.AND)

    if por_tipo_laudo:
        filtro.add(
            Q(id_requisicao__tipo_de_laudo__tipo_laudo__contains=por_tipo_laudo), Q.AND)

    if por_especie:
        filtro.add(
            Q(id_requisicao__id_animal__id_especie__nome_especie__contains=por_especie), Q.AND)

    if por_raca:
        filtro.add(
            Q(id_requisicao__id_animal__raca__nome_raca__contains=por_raca), Q.AND)

    if morfologico:
        filtro.add(Q(diagnostico_morfologico__icontains=morfologico), Q.AND)

    if por_estado:
        filtro.add(
            Q(id_requisicao__id_animal__id_estado__nome_estado__contains=por_estado), Q.AND)

    if por_cidade:
        filtro.add(
            Q(id_requisicao__id_animal__cidade__nome_cidade__contains=por_cidade), Q.AND)

    # if por_bairro:
    #     filtro.add(Q(id_requisicao__id_animal__rua__id_bairro__nome_bairro__contains=por_bairro), Q.AND)
    #
    # if por_rua:
    #     filtro.add(Q(id_requisicao__id_animal__rua__nome_rua__icontains=por_rua), Q.AND)

    if data_min:
        d_min = datetime.strptime(data_min, "%Y-%m-%d")
        filtro.add(Q(dt_laudo__gte=d_min), Q.AND)

    if data_max:
        d_max = datetime.strptime(data_max, "%Y-%m-%d")
        filtro.add(Q(dt_laudo__lte=d_max), Q.AND)

    laudos = LaudoModel.objects.filter(filtro)

    estados_ocorrencia = LaudoModel.objects.filter(filtro).distinct(
        'id_requisicao__id_animal__id_estado').count()
    estados_nomes = LaudoModel.objects.filter(filtro).distinct(
        'id_requisicao__id_animal__id_estado')
    cidades_ocorrencia = LaudoModel.objects.filter(filtro).distinct(
        'id_requisicao__id_animal__cidade').count()
    cidades_nome = LaudoModel.objects.filter(filtro).distinct(
        'id_requisicao__id_animal__cidade__nome_cidade')
    bairros_ocorrencia = LaudoModel.objects.filter(filtro).distinct(
        'id_requisicao__id_animal__bairro').count()
    ruas_ocorrencia = LaudoModel.objects.filter(filtro).distinct(
        'id_requisicao__id_animal__rua').count()

    relatorio = LaudoModel.objects.filter(filtro).count()

    c = filtro.children
    rel = []

    for d in c:
        lista_relatorio = list(d)
        rel.append(lista_relatorio[1])

    mapa = folium.Map(
        location=[-16.1237611, -59.9219642],
        zoom_start=4
    )

    estados_lista = []
    for caso in estados_nomes:
        estados_lista.append(
            caso.id_requisicao.id_animal.id_estado.nome_estado)

    cidades = []
    for caso in cidades_nome:
        cidades.append(caso.id_requisicao.id_animal.cidade.nome_cidade)

    df = pd.read_csv("templates/municipios.csv")
    for index, linha in df.iterrows():
        for c in cidades:
            if c == linha["nome"]:
                HeatMap([[linha['latitude'], linha['longitude']]], radius=30
                #folium.Marker(
                #    location=[linha['latitude'], linha['longitude']],
                #    popup=c
                ).add_to(mapa)

    mapa.save("templates/mapa.html")
    total_laudos = LaudoModel.objects.all().count()


    paginator = Paginator(laudos, 10)
    page = request.GET.get('page')
    list_laudos = paginator.get_page(page)

    return render(request, 'pagina_filtro_laudos.html', {'laudos': list_laudos, 'lista_sistemas': lista_sistemas,
                                                         'especies': especies, 'lista_raca': lista_raca,
                                                         'estados': estados, 'lista_cidade': lista_cidade,
                                                         'por_rua': por_rua, 'por_bairro': por_bairro,
                                                         'tipo_laudo': tipo_laudo,
                                                         'total_laudos': total_laudos, 'relatorio': relatorio,
                                                         'rel': rel, 'estados_ocorrencia': estados_ocorrencia,
                                                         'cidades_ocorrencia': cidades_ocorrencia,
                                                         'bairros_ocorrencia': bairros_ocorrencia,
                                                         'ruas_ocorrencia': ruas_ocorrencia, 'cidades_nome': cidades_nome,
                                                         'estados_lista': estados_lista})


def mapa(request):
    return render(request, "mapa.html")
