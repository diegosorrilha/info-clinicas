from django.shortcuts import render
from django.http import HttpResponse


def operador(request):

    return render(request, 'operador.html')
