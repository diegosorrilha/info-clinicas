from django.shortcuts import render

def cadastrar_paciente(request):

    context = {}
    
    return render(request, 'cadastrar_paciente.html', context)
