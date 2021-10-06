from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin,
)


class OperadorManager(BaseUserManager):

    def create_user(self, email, password=None):
        operador = self.model(
            email=self.normalize_email(email)
        )

        operador.is_active = True
        operador.is_staff = False
        operador.is_superuser = False

        if password:
            operador.set_password(password)

        operador.save()

        return operador

    def create_superuser(self, email, password):
        operador = self.create_user(
            email=self.normalize_email(email),
            password=password
        )
        operador.is_active = True
        operador.is_staff = True
        operador.is_superuser = True

        operador.set_password(password)

        operador.save()

        return operador


class Operador(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name="E-mail do Operador",
        max_length=194,
        unique=True,
    )
    is_active = models.BooleanField(
        verbose_name="Operador está ativo",
        default=True,
    )

    is_staff = models.BooleanField(
        verbose_name="Operador é da equipe de desenvolvimento ",
        default=False,
    )

    is_superuser = models.BooleanField(
        verbose_name="Operador é um superusuario",
        default=False,
    )

    USERNAME_FIELD = 'email'

    objects = OperadorManager()

    class Meta:
        verbose_name = "Operador"
        verbose_name_plural = "Operadores"
        db_table = "operador"
