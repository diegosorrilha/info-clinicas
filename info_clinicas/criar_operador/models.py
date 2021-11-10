from django.db import models
from django.db.models.base import Model
from django.utils.translation import ugettext as _
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin


class Operador(models.Model):

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
    email = models.EmailField(
        verbose_name="E-mail",
        max_length=194,
        blank=True,
        null=True,
    )

    usuario = models.CharField(
        verbose_name="Login",
        max_length=50,
        blank=False,
        null=False
    )

    senha = models.CharField(
        verbose_name="Senha",
        max_length=15,
        blank=False,
        null=False
    )

    confirme_senha = models.CharField(
        verbose_name="Confirme a Senha",
        max_length=15,
        blank=False,
        null=False
    )

    clinica_id = models.CharField(
        verbose_name="Id clinica",
        max_length=10,
    )

    observacao = models.CharField(
        verbose_name="Observacao",
        max_length=200,

    )

    class Meta:
        verbose_name = "Operador"
        verbose_name_plural = "Operadores"
        db_table = "operador"

    def __str__(self):
        return self.nome_completo
