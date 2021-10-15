from django.shortcuts import render
from django.http import HttpResponse


def criar_operador(request):

    return render(request, 'criar_operador.html')
