from django.shortcuts import (
    render, get_object_or_404, redirect
)
from django.contrib import messages

from info_clinicas.agendamento.models import Agendamento
from info_clinicas.especialidade.models import Especialidade
from info_clinicas.medicos.models import Disponibilidade
from info_clinicas.pacientes.models import Paciente

def agendar_consulta(request):

    error = False
    disponibilidades = Disponibilidade.objects.all()
    especialidade = Especialidade.objects.all()[0]
    pacientes = Paciente.objects.all()
    agendamentos = Agendamento.objects.all()
    

    if request.method == 'POST':
        
        disponibilidade_id = request.POST['disp_id']
        if disponibilidade_id == 'default':
            disponibilidade = None
        else:
            disponibilidade = Disponibilidade.objects.get(id=request.POST['disp_id'])
        
        paciente_id = request.POST['paciente_id']
        
        if paciente_id == 'default':
            paciente = None
        
        else:
            paciente = Paciente.objects.get(id=request.POST['paciente_id'])
        
        if disponibilidade and paciente:
            agendamento = Agendamento(agendado_para=disponibilidade, medico=disponibilidade.medico, paciente=paciente)
            agendamento.save()
            
        else:
            error = 'Agendamento não efetuado, tente novamente'

    context = {
        'disponibilidades': disponibilidades,
        'especialidade': especialidade.nome_especialidade,
        'pacientes': pacientes,
        'error': error,
        'agendamentos': agendamentos,
    }
    
    return render(request, 'agendar_consulta.html', context)

def cancelar_consulta(request, id):

    
    agendamento = get_object_or_404(
        Agendamento,
        id=id
    ) 

    agendamento.status = "CANCELADO"

    agendamento.save()

    messages.success(
        request,
        "Consulta cancelada com sucesso!"
    )

    return redirect("agendar_consulta")