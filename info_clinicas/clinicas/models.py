from django.db import models


class Clinica(models.Model):
    nome = models.CharField(
        verbose_name='Nome da clínica',
        max_length=194
    )

    cnpj = models.CharField(
        verbose_name='CPF',
        max_length=100
    )

    site = models.CharField(
        verbose_name='Site',
        max_length=50
    )

    endereco = models.CharField(
        verbose_name="Endereço (rua, número e bairro)",
        max_length=194,
    )

    cidade = models.CharField(
        verbose_name="Cidade",
        max_length=194,
    )

    estado = models.CharField(
        verbose_name="Estado",
        max_length=194,
    )

    telefone = models.CharField(
        verbose_name='Telefone de contato',
        max_length=11
    )

    responsavel = models.CharField(
        verbose_name='Nome do responsável',
        max_length=194
    )

    class Meta:
        verbose_name = 'Clínica'
        verbose_name_plural = 'Clínicas'
        db_table = 'clinica'

    def __str__(self):
        return f'{self.id} - {self.nome}'
