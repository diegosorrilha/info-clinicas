# Generated by Django 3.2.6 on 2021-08-31 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0002_paciente_sexo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='sexo',
            field=models.CharField(choices=[('M', 'masculino'), ('F', 'feminino')], default=None, max_length=9, verbose_name='Sexo'),
        ),
    ]
