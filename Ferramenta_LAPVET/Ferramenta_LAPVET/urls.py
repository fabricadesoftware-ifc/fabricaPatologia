"""Ferramenta_LAPVET URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from laudosMedvet import views

from django.conf import settings
from django.conf.urls.static import static

import laudosMedvet.views.especie_view
import laudosMedvet.views.proprietario_view
import laudosMedvet.views.veterinario_responsavel_view
import laudosMedvet.views.rua_view
import laudosMedvet.views.bairro_view
import laudosMedvet.views.cidade_view
import laudosMedvet.views.regiao_estado_view
import laudosMedvet.views.regiao_federal_view
import laudosMedvet.views.estado_view
import laudosMedvet.views.animal_view

import laudosMedvet.views.tipo_laudo_view
import laudosMedvet.views.imagem_view
import laudosMedvet.views.requisicao_laudo_view
import laudosMedvet.views.laudo_view

import laudosMedvet.views.consulta_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login', views.LoginView.as_view(), name='login'),
    path('logout', views.LogoutView.as_view(), name='logout'),
    path('cadastro/usuario/', views.CadastroUsuarioView.as_view(), name='cadastro_usuario'),
    path('', views.LoginUserView.as_view(), name="login_user"),
    path('principal/', views.PaginaPrincipal.as_view(), name='principal'),

    #animal
    path('animal/', views.animal_view.index_animal, name='index_animal'),
    path('animal/save/', views.animal_view.new_animal, name='new_animal'),
    path('animal/update/<int:id>', views.animal_view.update_animal, name='update_animal'),
    path('animal/delete/<int:id>', views.animal_view.delete_animal, name='delete_animal'),

    #Especie
    path('especie/', views.especie_view.index_especie, name='index_especie'),
    path('especie/save/', views.especie_view.new_especie, name='new_especie'),
    path('especie/update/<int:id>', views.especie_view.update_especie, name='update_especie'),
    path('especie/delete/<int:id>', views.especie_view.delete_especie, name='delete_especie'),

    #Pessoas
    path('pessoa/proprietario/', views.proprietario_view.index_proprietario, name='index_proprietario'),
    path('pessoa/proprietario/new/', views.proprietario_view.new_proprietario, name='new_proprietario'),
    path('pessoa/proprietario/update/<int:id>', views.proprietario_view.update_proprietario, name='update_proprietario'),
    path('pessoa/proprietario/delete/<int:id>', views.proprietario_view.delete_proprietario, name='delete_proprietario'),

    path('pessoa/veterinario/', views.veterinario_responsavel_view.index_vet_resp, name='index_vet_resp'),
    path('pessoa/veterinario/new/', views.veterinario_responsavel_view.new_vet_resp, name='new_vet_resp'),
    path('pessoa/veterinario/update/<int:id>', views.veterinario_responsavel_view.update_vet_resp, name='update_vet_resp'),
    path('pessoa/veterinario/delete/<int:id>', views.veterinario_responsavel_view.delete_vet_resp, name='delete_vet_resp'),

    #enderecos
    path('endereco/federal/', views.regiao_federal_view.index_regiao_fed, name='index_regiao_fed'),
    path('endereco/federal/new/', views.regiao_federal_view.new_regiao_fed, name='new_regiao_fed'),
    path('endereco/federal/update/<int:id>', views.regiao_federal_view.update_regiao_fed, name='update_regiao_fed'),
    path('endereco/federal/delete/<int:id>', views.regiao_federal_view.delete_regiao_fed, name='delete_regiao_fed'),

    path('endereco/estado/', views.estado_view.index_estado, name='index_estado'),
    path('endereco/estado/new/', views.estado_view.new_estado, name='new_estado'),
    path('endereco/estado/update/<int:id>', views.estado_view.update_estado, name='update_estado'),
    path('endereco/estado/delete/<int:id>', views.estado_view.delete_estado, name='delete_estado'),

    path('endereco/regiao/', views.regiao_estado_view.index_regiao_est, name='index_regiao_est'),
    path('endereco/regiao/new/', views.regiao_estado_view.new_regiao_est, name='new_regiao_est'),
    path('endereco/regiao/update/<int:id>', views.regiao_estado_view.update_regiao_est, name='update_regiao_est'),
    path('endereco/regiao/delete/<int:id>', views.regiao_estado_view.delete_regiao_est, name='delete_regiao_est'),

    path('endereco/cidade/', views.cidade_view.index_cidade, name='index_cidade'),
    path('endereco/cidade/new/', views.cidade_view.new_cidade, name='new_cidade'),
    path('endereco/cidade/update/<int:id>', views.cidade_view.update_cidade, name='update_cidade'),
    path('endereco/cidade/delete/<int:id>', views.cidade_view.delete_cidade, name='delete_cidade'),

    path('endereco/bairro/', views.bairro_view.index_bairro, name='index_bairro'),
    path('endereco/bairro/new/', views.bairro_view.new_bairro, name='new_bairro'),
    path('endereco/bairro/update/<int:id>', views.bairro_view.update_bairro, name='update_bairro'),
    path('endereco/bairro/delete/<int:id>', views.bairro_view.delete_bairro, name='delete_bairro'),

    path('endereco/rua/', views.rua_view.index_rua, name='index_rua'),
    path('endereco/rua/new/', views.rua_view.new_rua, name='new_rua'),
    path('endereco/rua/update/<int:id>', views.rua_view.update_rua, name='update_rua'),
    path('endereco/rua/delete/<int:id>', views.rua_view.delete_rua, name='delete_rua'),

    #tipo de laudo
    path('laudo/tipo/', views.tipo_laudo_view.index_tipo_laudo, name='index_tipo_laudo'),
    path('laudo/tipo/new/', views.tipo_laudo_view.new_tipo_laudo, name='new_tipo_laudo'),
    path('laudo/tipo/update/<int:id>', views.tipo_laudo_view.update_tipo_laudo, name='update_tipo_laudo'),
    path('laudo/tipo/delete/<int:id>', views.tipo_laudo_view.delete_tipo_laudo, name='delete_tipo_laudo'),

    #imagem
    path('laudo/imagem/', views.imagem_view.index_imagem, name='index_imagem'),
    path('laudo/imagem/new/', views.imagem_view.new_imagem, name='new_imagem'),
    path('laudo/imagem/update/<int:id>', views.imagem_view.update_imagem, name='update_imagem'),
    path('laudo/imagem/delete/<int:id>', views.imagem_view.delete_imagem, name='delete_imagem'),

    #requisição
    path('laudo/requisicao/', views.requisicao_laudo_view.index_requisicao, name='index_requisicao'),
    path('laudo/requisicao/new/', views.requisicao_laudo_view.new_requisicao, name='new_requisicao'),
    path('laudo/requisicao/update/<int:id>', views.requisicao_laudo_view.update_requisicao, name='update_requisicao'),
    path('laudo/requisicao/delete/<int:id>', views.requisicao_laudo_view.delete_requisicao, name='delete_requisicao'),

    #requisição
    path('laudo/', views.laudo_view.index_laudo, name='index_laudo'),
    path('laudo/new/', views.laudo_view.new_laudo, name='new_laudo'),
    path('laudo/update/<int:id>', views.laudo_view.update_laudo, name='update_laudo'),
    path('laudo/delete/<int:id>', views.laudo_view.delete_laudo, name='delete_laudo'),

    #consultas
    path('consulta/requisicao/', views.consulta_view.consulta_requisicao, name='consulta_requisicao'),
    path('consulta/requisicao/<int:id>', views.consulta_view.visualizar_requisicao, name='visualizar_requisicao'),
    path('consulta/laudo/', views.consulta_view.consulta_laudo, name='consulta_laudo'),
    path('consulta/laudo/<int:id>', views.consulta_view.visualizar_laudo, name='visualizar_laudo'),
    path('consulta/laudo/imagens/<int:id>', views.consulta_view.visualizar_imagens, name='visualizar_imagens'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)