from django.shortcuts import render
from info_clinicas.agendamento.models import Agendamento

def agendar_consulta(request):

    return render(request, 'agendar_consulta.html')
