# coding:utf-8
from django.db.models import Q
from django.shortcuts import redirect, render, get_object_or_404
from ..models import LaudoModel, ImagensModel
from django.contrib.auth.decorators import login_required


from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.template.loader import render_to_string

from weasyprint import HTML


@login_required
def gera_pdf(request, id):
    laudo = get_object_or_404(LaudoModel, pk=id)
    imagens = ImagensModel.objects.filter(id_laudo=id)

    lista_imagens = request.GET.getlist('lista_imagens', None)

    print(lista_imagens)

    return render(request, 'gerar_pdf_filtro.html', {'laudo': laudo, 'imagens':imagens})


@login_required
def html_to_pdf_view(request, id):

    laudo = get_object_or_404(LaudoModel, pk=id)
    imagens = ImagensModel.objects.all().filter(id_laudo=id)
    html_string = render_to_string('consultas/pdf_laudo_template.html', {'laudo': laudo, 'imagens':imagens})

    html = HTML(string=html_string, base_url=request.build_absolute_uri())
    html.write_pdf(target='/tmp/'+str(laudo.id))

    fs = FileSystemStorage('/tmp')
    with fs.open(str(laudo.id)) as pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="laudo"'
        return response
    return response
