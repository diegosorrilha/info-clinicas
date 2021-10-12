from django.shortcuts import render, redirect
from info_clinicas.especialidade.models import Especialidade


def cadastrar_especialidade(request):

    if request.method == "POST":
        nomeespecialidade = request.POST['nome-especialidade']
        datainclusao = request.POST['data-inclusao']

        inclu = Especialidade(
            nome_especialidade=nomeespecialidade.lower(),
            data_inclusao=datainclusao,

        )

        inclu.save()

        return redirect("cadastrar_especialidade")

    return render(request, 'especialidade.html')
