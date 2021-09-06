from django.shortcuts import render
from info_clinicas.medicos.models import Medicos

def cadastrar_medico(request):
    if request.method == 'POST':
        n_c = request.POST['nome-completo']
        crm = request.POST['CRM']
        tel = request.POST['telefone']
        email = request.POST['email']
        endereço = request.POST['endereço']
        cidade = request.POST['cidade']
        estado = request.POST['estado']
        bairro = request.POST['bairro']
        pais = request.POST['pais']
        sexo = request.POST['sexo']
        datanascimento = request.POST['data-nascimento']

        medico = Medicos(
            nome_completo=n_c.lower(),
            crm=crm,
            telefone=tel,
            email=email,
            endereço=endereço.lower(),
            bairro=bairro,
            cidade=cidade.lower(),
            estado=estado.lower(),
            pais=pais,
            sexo=sexo,
            data_nascimento=datanascimento,
        )

        medico.save()

        return redirect("cadastrar_medico")

    return render(request, 'cadastrar_medico.html')