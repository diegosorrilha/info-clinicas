from django.db import models

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

    class Meta:
        verbose_name = "Agendamento"
        verbose_name_plural = "Agendamentos"
        db_table = "agendamento"
