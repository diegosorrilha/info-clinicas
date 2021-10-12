from django.shortcuts import render, redirect

from info_clinicas.clinicas.models import Clinica


def cadastrar_clinica(request):
    if request.method == 'POST':
        nome = request.POST['nome_clinica']
        cnpj = request.POST['cpnj']
        site = request.POST['site']
        endereco = request.POST['endereco']
        cidade = request.POST['cidade']
        estado = request.POST['estado']
        telefone = request.POST['telefone']
        responsavel = request.POST['responsavel']

        clinica = Clinica(
            nome=nome,
            cnpj=cnpj,
            site=site,
            endereco=endereco,
            cidade=cidade,
            estado=estado,
            telefone=telefone,
            responsavel=responsavel,
        )

        clinica.save()

        return redirect("cadastrar_clinica")

    return render(request, 'cadastrar-clinica.html')
