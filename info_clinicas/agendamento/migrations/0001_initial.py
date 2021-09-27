# Generated by Django 3.2.6 on 2021-09-27 22:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pacientes', '0004_alter_paciente_sexo'),
        ('medicos', '0003_auto_20210927_1934'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agendamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('AGENDADO', 'Agendado'), ('CONSULTADO', 'Consultado')], default='AGENDADO', max_length=126, verbose_name='Status de agendamento')),
                ('agendado_para', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='medicos.disponibilidade')),
                ('medico', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='medicos.medicos')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pacientes.paciente')),
            ],
            options={
                'verbose_name': 'Agendamento',
                'verbose_name_plural': 'Agendamentos',
                'db_table': 'agendamento',
            },
        ),
    ]
