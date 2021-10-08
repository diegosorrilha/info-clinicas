from django.db import models

from info_clinicas.clinicas.models import Clinica

class Agendamento(models.Model):

    STATUS_AGENDAMENTO = [
        ("AGENDADO", "Agendado"),
        ("CONSULTADO", "Consultado"),
        ("CANCELADO", "Cancelado"),
    ]

    status = models.CharField(
        verbose_name="Status de agendamento",
        max_length=126,
        choices=STATUS_AGENDAMENTO,
        default="AGENDADO",
    )
    
    agendado_para = models.ForeignKey(
        "medicos.Disponibilidade",
        on_delete=models.PROTECT,
    )

    medico = models.ForeignKey(
        "medicos.Medicos",
        on_delete=models.PROTECT,
    )
    
    paciente = models.ForeignKey(
        "pacientes.Paciente",
        on_delete=models.PROTECT,
    )

    clinica = models.ForeignKey(Clinica, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = "Agendamento"
        verbose_name_plural = "Agendamentos"
        db_table = "agendamento"
    
    def get_hora(self):
        if self.agendado_para.hora:
            hora = str(self.agendado_para.hora)
            only_hora = hora[0:2]

            return only_hora
    
    def get_minutos(self):
        if self.agendado_para.hora:
            minuto = str(self.agendado_para.hora)
            only_minuto = minuto[3:5]

            if only_minuto == '01':
                return (f"e {only_minuto} minuto")
        
            elif only_minuto == '00':
                return ""
            
            else:
                return (f"e {only_minuto} minutos")