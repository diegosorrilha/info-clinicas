from django.shortcuts import render


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

        print(nome, cnpj, site, endereco, cidade, estado, telefone, responsavel)

    return render(request, 'cadastrar-clinica.html')
