
from info_clinicas.especialidade.models import Especialidade
from django.shortcuts import render


def cadastrar_especialidade(request):

    if request.method == "POST":
        nomeespecialidade = request.POST['nome_especialidade']
        datainclusao = request.POST['data_inclusao']

        print(nomeespecialidade, datainclusao)

    return render(request, 'especialidade.html')
