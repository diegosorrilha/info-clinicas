from django.contrib import admin
from info_clinicas.especialidade.models import Especialidade

admin.site.register(Especialidade)


class EspecialidadeAdmin(admin.ModelAdmin):
    list_display = ('nome_especialidade', 'data_inclusao', 'especialidade')
    list_filter = ('nome_especialidade')
    search_fields = ('nome_especialidade', 'data_inclusao', 'especialidade')
