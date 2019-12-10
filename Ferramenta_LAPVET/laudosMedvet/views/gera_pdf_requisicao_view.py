# coding:utf-8
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from laudosMedvet.models import RequisicaoLaudoModel

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML


@login_required
def gera_requisicao_pdf(request, id):
    requisicao = get_object_or_404(RequisicaoLaudoModel, pk=id)

    html_string = render_to_string('consultas/pdf_requisicao_template.html', {'requisicao': requisicao})

    html = HTML(string=html_string, base_url=request.build_absolute_uri())
    html.write_pdf(target='/tmp/' + str(requisicao.id))

    fs = FileSystemStorage('/tmp')
    with fs.open(str(requisicao.id)) as pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="requisicao"'
        return response
    return response