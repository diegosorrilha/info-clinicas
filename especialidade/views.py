from django.shortcuts import render
from especialidade.models import Especialidade


context = {
        "nome_pagina": "Cadastro de Especialidades",
}

return render("especialidade.html", context)
