"""info_clinicas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path

from info_clinicas.especialidade.views import cadastrar_especialidade
from info_clinicas.core.views import home
from info_clinicas.core.views import home, login
from info_clinicas.clinicas.views import cadastrar_clinica
from info_clinicas.pacientes.views import cadastrar_paciente
from info_clinicas.medicos.views import cadastrar_medico

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login, name='login'),
    path('', home, name='home'),

    path('cadastrar-especialidade', cadastrar_especialidade,
         name='cadastrar_especialidade'),

    path('cadastrar-clinica', cadastrar_clinica, name='cadastrar_clinica'),
    path('cadastrar-paciente/', cadastrar_paciente, name='cadastrar_paciente'),
    path('cadastrar-medico/', cadastrar_medico, name="cadastrar_medicos"),

]
