from django.shortcuts import render
# from django.http import HttpResponse


def cadastrar_especialidade(request):

    # return HttpResponse('<h1>Cadastrar Especialidades</h1>')
    return render(request, 'especialidade.html')
