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
import laudosMedvet.views.rua_view
import laudosMedvet.views.bairro_view
import laudosMedvet.views.cidade_view
import laudosMedvet.views.regiao_estado_view
import laudosMedvet.views.regiao_federal_view
import laudosMedvet.views.estado_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login', views.LoginView.as_view(), name='login'),
    path('logout', views.LogoutView.as_view(), name='logout'),
    path('cadastro/usuario/', views.CadastroUsuarioView.as_view(), name='cadastro_usuario'),
    path('', views.LoginUserView.as_view(), name="login_user"),
    path('principal/', views.PaginaPrincipal.as_view(), name='principal'),
    path('cadastro/animal/', views.AnimalView.as_view(), name='cadastrar_animal'),
    path('cadastro/laudo/', views.LaudoView.as_view(), name='cadastrar_laudo'),


    #Especie
    path('animal/', views.especie_view.index_especie, name='index_especie'),
    path('animal/save/', views.especie_view.new_especie, name='new_especie'),
    path('animal/update/<int:id>', views.especie_view.update_especie, name='update_especie'),
    path('animal/delete/<int:id>', views.especie_view.delete_especie, name='delete_especie'),

    #Pessoas
    path('pessoa/proprietario/', views.proprietario_view.index_proprietario, name='index_proprietario'),
    path('pessoa/proprietario/new/', views.proprietario_view.new_proprietario, name='new_proprietario'),
    path('pessoa/proprietario/update/<int:id>', views.proprietario_view.update_proprietario, name='update_proprietario'),
    path('pessoa/proprietario/delete/<int:id>', views.proprietario_view.delete_proprietario, name='delete_proprietario'),

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

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)