from django.shortcuts import render, redirect
from info_clinicas.criar_operador.models import Operador


def criar_operador(request):

    if request.method == "POST":
        nomecompleto = request.POST["nome-completo"]
        datanascimento = request.POST["data-nascimento"]
        telefoneoperador = request.POST["telefone-operador"]
        emailoperador = request.POST["Email"]
        usuariooperador = request.POST["usuario-operador"]
        senhaoperador = request.POST["senha-operador"]
        confirmesenha = request.POST["confirme-senha"]
        clinica_id = request.POST["clinica-id"]
        campoobservacao = request.POST["obs"]

        criar = Operador(
            nome_completo=nomecompleto,
            data_nascimento=datanascimento,
            telefone=telefoneoperador,
            email=emailoperador,
            usuario=usuariooperador,
            senha=senhaoperador,
            confirme_senha=confirmesenha,
            clinica_id=clinica_id,
            observacao=campoobservacao,
        )

        criar.save()

        # return redirect("criar_operador")

    return render(request, 'criar_operador.html')
