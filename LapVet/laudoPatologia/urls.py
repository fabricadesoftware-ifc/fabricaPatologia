from django.template.response import TemplateResponse
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import PaginaPrincipal, estado_view, cidade_view, bairro_view, rua_view, proprietario_view, \
    veterinario_responsavel_view, especie_view, raca_view, animal_view, tipo_laudo_view, requisicao_laudo_view, \
    laudo_view, imagem_view, veterinario_patologista_view, consulta_view, gera_pdf_laudo_view, gera_pdf_requisicao_view, \
    filtro_laudos_view, usuario_view

urlpatterns = [
    path('', PaginaPrincipal.as_view(), name='principal'),
    path('cadastro/', usuario_view.CadastroPrimeiroAcesso.as_view(), name='cadastro'),
    path('cadastro/update/<int:id>', usuario_view.update_usuario, name='update_usuario'),
    path('endereco/estado/', estado_view.index_estado, name='index_estado'),
    path('endereco/estado/new/', estado_view.new_estado, name='new_estado'),
    path('endereco/estado/update/<int:id>', estado_view.update_estado, name='update_estado'),
    path('endereco/estado/delete/<int:id>', estado_view.delete_estado, name='delete_estado'),

    path('endereco/cidade/', cidade_view.index_cidade, name='index_cidade'),
    path('endereco/cidade/new/', cidade_view.new_cidade, name='new_cidade'),
    path('endereco/cidade/update/<int:id>', cidade_view.update_cidade, name='update_cidade'),
    path('endereco/cidade/delete/<int:id>', cidade_view.delete_cidade, name='delete_cidade'),

    path('endereco/bairro/', bairro_view.index_bairro, name='index_bairro'),
    path('endereco/bairro/new/', bairro_view.new_bairro, name='new_bairro'),
    path('endereco/bairro/update/<int:id>', bairro_view.update_bairro, name='update_bairro'),
    path('endereco/bairro/delete/<int:id>', bairro_view.delete_bairro, name='delete_bairro'),

    path('endereco/rua/', rua_view.index_rua, name='index_rua'),
    path('endereco/rua/new/', rua_view.new_rua, name='new_rua'),
    path('endereco/rua/update/<int:id>', rua_view.update_rua, name='update_rua'),
    path('endereco/rua/delete/<int:id>', rua_view.delete_rua, name='delete_rua'),

    path('pessoa/proprietario/', proprietario_view.index_proprietario, name='index_proprietario'),
    path('pessoa/proprietario/new/', proprietario_view.new_proprietario, name='new_proprietario'),
    path('pessoa/proprietario/update/<int:id>', proprietario_view.update_proprietario,
       name='update_proprietario'),
    path('pessoa/proprietario/delete/<int:id>', proprietario_view.delete_proprietario,
       name='delete_proprietario'),

    path('pessoa/veterinario/', veterinario_responsavel_view.index_vet_resp, name='index_vet_resp'),
    path('pessoa/veterinario/new/', veterinario_responsavel_view.new_vet_resp, name='new_vet_resp'),
    path('pessoa/veterinario/update/<int:id>', veterinario_responsavel_view.update_vet_resp,
       name='update_vet_resp'),
    path('pessoa/veterinario/delete/<int:id>', veterinario_responsavel_view.delete_vet_resp,
       name='delete_vet_resp'),

    path('especie/', especie_view.index_especie, name='index_especie'),
    path('especie/save/', especie_view.new_especie, name='new_especie'),
    path('especie/update/<int:id>', especie_view.update_especie, name='update_especie'),
    path('especie/delete/<int:id>', especie_view.delete_especie, name='delete_especie'),

    path('raca/', raca_view.index_raca, name='index_raca'),
    path('raca/save/', raca_view.new_raca, name='new_raca'),
    path('raca/update/<int:id>', raca_view.update_raca, name='update_raca'),
    path('raca/delete/<int:id>', raca_view.delete_raca, name='delete_raca'),

    path('animal/', animal_view.index_animal, name='index_animal'),
    path('animal/save/', animal_view.new_animal, name='new_animal'),
    path('animal/update/<int:id>', animal_view.update_animal, name='update_animal'),
    path('animal/delete/<int:id>', animal_view.delete_animal, name='delete_animal'),
    path('ajax/load-racas/', animal_view.load_racas, name='ajax_load_racas'),
    path('ajax/load-cidade/', animal_view.load_cidade, name='ajax_load_cidade'),
    path('ajax/load-bairro/', animal_view.load_bairro, name='ajax_load_bairro'),
    path('ajax/load-rua/', animal_view.load_rua, name='ajax_load_rua'),

    path('laudo/tipo/', tipo_laudo_view.index_tipo_laudo, name='index_tipo_laudo'),
    path('laudo/tipo/new/', tipo_laudo_view.new_tipo_laudo, name='new_tipo_laudo'),
    path('laudo/tipo/update/<int:id>', tipo_laudo_view.update_tipo_laudo, name='update_tipo_laudo'),
    path('laudo/tipo/delete/<int:id>', tipo_laudo_view.delete_tipo_laudo, name='delete_tipo_laudo'),

    path('laudo/requisicao/', requisicao_laudo_view.index_requisicao, name='index_requisicao'),
    path('laudo/requisicao/new/', requisicao_laudo_view.new_requisicao, name='new_requisicao'),
    path('laudo/requisicao/update/<int:id>', requisicao_laudo_view.update_requisicao, name='update_requisicao'),
    path('laudo/requisicao/delete/<int:id>', requisicao_laudo_view.delete_requisicao, name='delete_requisicao'),

    path('laudo/patologista/', veterinario_patologista_view.index_vet_pat, name='index_vet_pat'),
    path('laudo/patologista/new/', veterinario_patologista_view.new_vet_pat, name='new_vet_pat'),
    path('laudo/patologista/update/<int:id>', veterinario_patologista_view.update_vet_pat, name='update_vet_pat'),
    path('laudo/patologista/delete/<int:id>', veterinario_patologista_view.delete_vet_pat, name='delete_vet_pat'),


    path('laudo/', laudo_view.index_laudo, name='index_laudo'),
    path('laudo/new/', laudo_view.new_laudo, name='new_laudo'),
    path('laudo/update/<int:id>', laudo_view.update_laudo, name='update_laudo'),
    path('laudo/delete/<int:id>', laudo_view.delete_laudo, name='delete_laudo'),

    path('laudo/imagem/', imagem_view.index_imagem, name='index_imagem'),
    path('laudo/imagem/new/', imagem_view.new_imagem, name='new_imagem'),
    path('laudo/imagem/update/<int:id>', imagem_view.update_imagem, name='update_imagem'),
    path('laudo/imagem/delete/<int:id>', imagem_view.delete_imagem, name='delete_imagem'),

    path('consulta/requisicao/', consulta_view.consulta_requisicao, name='consulta_requisicao'),
    path('consulta/requisicao/<int:id>', consulta_view.visualizar_requisicao, name='visualizar_requisicao'),
    path('consulta/laudo/', consulta_view.consulta_laudo, name='consulta_laudo'),
    path('consulta/laudo/<int:id>', consulta_view.visualizar_laudo, name='visualizar_laudo'),
    path('consulta/laudo/imag/<int:id>', consulta_view.visualizar_imagens_por_laudo, name='visualizar_imagens_por_laudo'),

    path('pdf-view/<int:id>', gera_pdf_laudo_view.html_to_pdf_view, name='seleciona_pdf'),
    path('gera_pdf/<int:id>', gera_pdf_laudo_view.gera_pdf, name='gera_pdf'),
    path('requisicao_pdf/<int:id>', gera_pdf_requisicao_view.gera_requisicao_pdf, name='requisicao_pdf'),

    path('procura/', filtro_laudos_view.lista_laudos, name="procura_laudos"),

    path('mapa/', filtro_laudos_view.mapa, name="mapa"),

    path('^', TemplateResponse, {'template':'erro_404.html'}),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)