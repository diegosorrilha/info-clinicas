from django.db import models


class Especialidade(models.Model):

    nome_especialidade = models.CharField(
        verbose_name="Especialidade",
        max_length=194,
    )

    data_inclusao = models.DateTimeField(
        verbose_name='Data Inclusao',
        auto_now_add=False,
        auto_now=True,
    )

    def __str__(self):
        return f'{self.id} - {self.nome_especialidade}'
