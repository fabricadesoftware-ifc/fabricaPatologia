# coding:utf-8

import os
import errno
from django.shortcuts import redirect, render, get_object_or_404


from laudosMedvet.models import LaudoModel
from django.contrib.auth.decorators import login_required
import pdfkit

@login_required
def gera_laudo_pdf(request, id):
    laudo = get_object_or_404(LaudoModel, pk=id)

    options = {
        'margin-top': '0.75in',
        'margin-right': '0.75in',
        'margin-bottom': '0.75in',
        'margin-left': '0.75in',
        'encoding': "pt_BR.utf-8",
    }
    # TODO:colocar imagem de logo no pdf

    texto = "<meta http-equiv='Content-Type' content='text/html; charset=utf-8'>" \
            "</div><div style='float: left; width: 10%'>Logo</div>" \
            "</div><div style='float: right; width: 10%'> Nº </div>" \
            "<img src='static/image/ifc.png' width='10%' height='10%'/>" + \
            "<p style='text-align: center;'>INSTITUTO FEDERAL CATARINENSE</p>" \
            "<p style='text-align: center;'>CAMPUS ARAQUARI</p>" \
            "<p style='text-align: center;'>LABORATÓRIO DE ANATOMIA E PATOLOGIA VETERINÁRIA</p>" \
            "<hr><h3 style='text-align: center;'><div style='text-transform: uppercase;'>\
            LAUDO DE " + laudo.id_requisicao.tipo_de_laudo.tipo_laudo + "</div></h3><hr>" \
            + "<p style='text-align: justified;'><div style='float: left; width: 40%'>Nome: " + laudo.id_requisicao.cod_animail.nome \
            + "</div> Espécie: " + laudo.id_requisicao.cod_animail.raca.id_especie.nome_especie + "<div style='float: right; width: 30%'> " \
                                                                                                  "Raça: " + laudo.id_requisicao.cod_animail.raca.nome_raca + "</div>" \
            + "<br>" + "<div style='float: left; width: 40%'>Data de nascimento: " + str(
        laudo.id_requisicao.cod_animail.idade) + "</div>" \
            + "Sexo: " + laudo.id_requisicao.cod_animail.sexo + "<div style='float: right; width: 30%'>Pelagem: " + laudo.id_requisicao.cod_animail.cor_pelagem \
            + "</div><p style='text-align: justified;'><div style='float: left; width: 40%'>Proprietário: " \
            + laudo.id_requisicao.cod_animail.proprietario.nome_proprietario \
            + "</div>Telefone: " + str(
        laudo.id_requisicao.cod_animail.proprietario.telefone) + "<div style='float: right; width: 30%'>Celular: " \
            + str(laudo.id_requisicao.cod_animail.proprietario.celular) \
            + "</div> Endereço: Rua "\
            + " Bairro: " + " Cidade: " \
            + " Estado: " \
            + "<p style='text-align: justified;'><div style='float: left; width: 40%'>Veterinário Responsável: " + laudo.id_requisicao.cod_animail.veterinario_responsavel.nome_veterinario \
            + "</div><div style='float: right; width: 30%'>Telefone: " + str(
        laudo.id_requisicao.cod_animail.veterinario_responsavel.telefone) + "</div><br></p>" \
            + "<p style='text-align: center;'><u><b>MATERIAL ENVIADO PARA EXAME</b></u></p>" \
            + laudo.id_requisicao.material_enviado + "<br><b> Data da coleta: </b>" + str(laudo.id_requisicao.dt_coleta) \
            + "<p style='text-align: center;'><u><b>HISTÓRICO CLÍNICO</b></u></p>" + laudo.id_requisicao.historico_clinico \
            + "<p style='text-align: center;'><u><b>DESCRIÇÃO MACROSCÓPICA</b></u></p>" + laudo.id_requisicao.descricao_macroscopica + "<br><br>" \
            + "<p style='text-align: justified;'>" \
            + "<p style='text-align: center;'><u><b>DESCRIÇÃO MICROSCÓPICA</b></u></p>" + laudo.descricao_microscopica + "<br><br>" \
            + "<p style='text-align: justified;'>" \
            + "<p style='text-align: center;'><u><b>DIAGNÓSTICO MORFOLÓGICO</b></u></p>" + laudo.diagnostico_morfologico + "<br><br>" \
            + "<p style='text-align: justified;'>" \
            + "<p style='text-align: center;'><u><b>COMENTÁRIOS</b></u></p>" + laudo.comentarios + "<br><br>"\
            + "<p style='text-align: center;'> Araquari," + str(laudo.dt_laudo) + \
            "<p style='text-align: center;'>" + laudo.veterinario_patologista.nome + \
            "<br>" + laudo.veterinario_patologista.formacao + \
            "<br>" + laudo.veterinario_patologista.crmv + "</p>"


    n = LaudoModel.id

    BASE_NAME = "static/media/laudos/"

    try:
        os.makedirs(BASE_NAME)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise

    MEDIA_NAME = os.path.join(BASE_NAME, "%s.pdf" % n)
    pdfkit.from_string(texto, MEDIA_NAME, options=options)

    return redirect("/" + MEDIA_NAME)