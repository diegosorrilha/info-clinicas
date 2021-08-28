from django.db import models


class Especialidade(models.Model):

    Nome_especialidade = models.CharField(
        verbose_name="Especialidade",
        max_length=194,
    )
