from django.db import models

class Paciente(models.Model):
    
    SEXO_ESCOLHA = [
        ("M", "masculino"),
        ("F", "feminino"),
        ("O", "outro"),
    ]
    
    sexo = models.CharField(
        verbose_name="Sexo",
        max_length=9,
        choices=SEXO_ESCOLHA,
        default=None,
    )

    nome_completo = models.CharField(
        verbose_name="Nome completo",
        max_length=194
    )

    data_nascimento = models.DateField(
        verbose_name="Data de nascimento",
        auto_now=False,
        auto_now_add=False,
    )
    
    telefone = models.CharField(
        verbose_name="Telefone",
        max_length=11,
    )

    endereço = models.CharField(
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

    email = models.EmailField(
        verbose_name="E-mail",
        max_length=194,
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Paciente"
        verbose_name_plural = "Pacientes"
        db_table = "paciente"
    
    def __str__(self):
        return self.nome_completo
