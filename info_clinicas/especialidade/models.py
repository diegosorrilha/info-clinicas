from django.db import models


class Especialidade(models.Model):

    Nome_especialidade = models.CharField(
        verbose_name="Especialidade",
        max_length=194,
    ),

    Data_inclusao = models.DateField(
        verbose_name='Data Inclusao',
        auto_now_add=False,
        auto_now=False,
    )
