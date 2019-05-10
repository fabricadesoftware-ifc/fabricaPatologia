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


#separar as partes em apps para melhorar a manutenção

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login', views.LoginView.as_view(), name='login'),
    path('logout', views.LogoutView.as_view(), name='logout'),
    path('cadastro/usuario/', views.CadastroUsuarioView.as_view(), name='cadastro_usuario'),
    path('', views.LoginUserView.as_view(), name="login_user"),
    path('principal/', views.PaginaPrincipal.as_view(), name='principal'),
    path('cadastro/especie/', views.AnimalView.as_view(), name='cadastrar_animal'),
    path('cadastro/laudo/', views.LaudoView.as_view(), name='cadastrar_laudo'),


    #Especie
    path('especie/', views.especie_view.index_especie, name='index_especie'),
    path('especie/save/', views.especie_view.new_especie, name='new_especie'),
    path('especie/update/<int:id>', views.especie_view.update_especie, name='update_especie'),
    path('especie/delete/<int:id>', views.especie_view.delete_especie, name='delete_especie'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)