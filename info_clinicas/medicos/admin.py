from django.contrib import admin
from info_clinicas.medicos.models import Medicos, Disponibilidade

admin.site.register(Medicos)
admin.site.register(Disponibilidade)