from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse(
        '<h1>Bem vindo ao Info Clinicas :)</h1>'
        '<p>Agora com ambieente de Desenvolvimento</p>'
    )
