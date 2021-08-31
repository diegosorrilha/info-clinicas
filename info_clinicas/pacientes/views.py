from django.shortcuts import render, redirect
from info_clinicas.pacientes.models import Paciente

def cadastrar_paciente(request):
    if request.method == 'POST':
        n_c = request.POST['nome-completo'] 
        tel = request.POST['telefone']
        email = request.POST['email'] 
        endereço = request.POST['endereço']
        cidade = request.POST['cidade'] 
        estado = request.POST['estado'] 
        sexo = request.POST['sexo'] 
        datanascimento = request.POST['data-nascimento']
        
        paciente = Paciente(
            nome_completo=n_c.lower(),
            telefone=tel,
            email=email,
            endereço=endereço.lower(),
            cidade=cidade.lower(),
            estado=estado.lower(),
            sexo=sexo,
            data_nascimento=datanascimento,
        )

        paciente.save()

        return redirect("cadastrar_paciente")

    context = {}
    
    return render(request, 'cadastrar_paciente.html', context)
