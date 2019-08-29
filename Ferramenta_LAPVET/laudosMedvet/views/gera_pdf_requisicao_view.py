# coding:utf-8

import os
import errno
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from laudosMedvet.models import RequisicaoLaudoModel
import pdfkit


@login_required
def gera_requisicao_pdf(request, id):
    requisicao = get_object_or_404(RequisicaoLaudoModel, pk=id)

    options = {
        'margin-top': '0.75in',
        'margin-right': '0.75in',
        'margin-bottom': '0.75in',
        'margin-left': '0.75in',
        'encoding': "pt_BR.utf-8",
    }
    # TODO:colocar imagem de logo no pdf

    texto = "<img src='static/image/ifc.png' width='10%' height='10%'/>" + \
            "<meta http-equiv='Content-Type' content='text/html; charset=utf-8'>"\
            "<p style='text-align: center;'>INSTITUTO FEDERAL CATARINENSE</p>" \
            "<p style='text-align: center;'>CAMPUS ARAQUARI</p>" \
            "<p style='text-align: center;'>LABORATÓRIO DE ANATOMIA E PATOLOGIA VETERINÁRIA</p>" \
            "<hr><h3 style='text-align: center;'><div style='text-transform: uppercase;'>\
            REQUISIÇÃO DE "+ requisicao.tipo_de_laudo.tipo_laudo + "</div></h3><hr>" \
            + "<p style='text-align: justified;'><div style='float: left; width: 40%'>Nome: " + requisicao.cod_animail.nome \
            + "</div> Espécie: " + requisicao.cod_animail.raca.id_especie.nome_especie + "<div style='float: right; width: 30%'> " \
            "Raça: " + requisicao.cod_animail.raca.nome_raca + "</div>"\
            + "<br>" + "<div style='float: left; width: 40%'>Data de nascimento: " + str(requisicao.cod_animail.idade) + "</div>"\
            + "Sexo: " + requisicao.cod_animail.sexo + "<div style='float: right; width: 30%'>Pelagem: " + requisicao.cod_animail.cor_pelagem\
            + "</div><p style='text-align: justified;'><div style='float: left; width: 40%'>Proprietário: " \
            + requisicao.cod_animail.proprietario.nome_proprietario\
            + "</div>Telefone: " + str(requisicao.cod_animail.proprietario.telefone) + "<div style='float: right; width: 30%'>Celular: " \
            + str(requisicao.cod_animail.proprietario.celular) + "</div> Endereço: Rua " + requisicao.cod_animail.proprietario.rua.nome_rua\
            + " Bairro: " + requisicao.cod_animail.proprietario.rua.id_bairro.nome_bairro + " Cidade: "\
            + requisicao.cod_animail.proprietario.rua.id_bairro.id_cidade.nome_cidade + " Estado: "\
            + requisicao.cod_animail.proprietario.rua.id_bairro.id_cidade.id_estado.nome_estado\
            + "<p style='text-align: justified;'><div style='float: left; width: 40%'>Veterinário Responsável: " + requisicao.cod_animail.veterinario_responsavel.nome_veterinario\
            + "</div><div style='float: right; width: 30%'>Telefone: " + str(requisicao.cod_animail.veterinario_responsavel.telefone) + "</div><br>"\
            + "<p style='text-align: center;'><u><b>MATERIAL ENVIADO PARA EXAME</b></u></p>"\
            + requisicao.material_enviado + "<br><b> Data da coleta: </b>" + str(requisicao.dt_coleta) \
            + "<p style='text-align: center;'><u><b>HISTÓRICO CLÍNICO</b></u></p>" + requisicao.historico_clinico \
            + "<p style='text-align: center;'><u><b>DESCRIÇÃO MACROSCÓPICA</b></u></p>" + requisicao.descricao_macroscopica +"<br><br>" \
            + "<p style='text-align: justified;'>" \
            "<b>Assinatura do requisitante:</b>  ___________________________________________________________________<br>"\
            + "<div style='botton: 0;'><fieldset>" + "<div style='text-align: center;'><u><b>PARA USO DO LAPVET</b></u></div><br>"\
            + "<b>Número do registro: </b>" + str(requisicao.id) + "<br><b> Data do recebimento: </b>" + str(requisicao.dt_recebimento)\
            + "<br><b>Assinatura do responsável pelo recebimento:</b> ___________________________________________"\
            + "</fieldset></div>"


    n = RequisicaoLaudoModel.id

    BASE_NAME = "static/media/laudos/"

    try:
        os.makedirs(BASE_NAME)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise

    MEDIA_NAME = os.path.join(BASE_NAME, "%s.pdf" % n)
    pdfkit.from_string(texto, MEDIA_NAME, options=options)

    return redirect("/" + MEDIA_NAME)

# + "</div>Endereço: Rua " + requisicao.cod_animail.proprietario.rua + " Bairro: " + requisicao.cod_animail.proprietario.rua.id_bairro.nome_bairro\
#             + " Cidade: " + requisicao.cod_animail.proprietario.rua.id_bairro.id_cidade.nome_cidade \
#             + " Estado: " + requisicao.cod_animail.proprietario.rua.id_bairro.id_cidade.id_regiao_estado.id_estado.nome_estado\

