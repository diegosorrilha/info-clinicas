
from info_clinicas.especialidade.models import Especialidade
from django.shortcuts import render
# from django.http import HttpResponse


def cadastrar_especialidade(request):

    # return HttpResponse('<h1>Cadastrar Especialidades</h1>')
    if request.method == "POST":
        nomeespecialidade = request.POST['nome_especialidade']
        datainclusao = request.POST['data_inclusao']

        print(nomeespecialidade, datainclusao)

    return render(request, 'especialidade.html')
