# Generated by Django 3.2.6 on 2021-09-27 22:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('medicos', '0002_auto_20210901_2023'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='medicos',
            options={},
        ),
        migrations.AlterModelTable(
            name='medicos',
            table=None,
        ),
        migrations.CreateModel(
            name='Disponibilidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('data', models.DateField(verbose_name='Data disponível')),
                ('hora', models.DateTimeField(verbose_name='Horário disponível')),
                ('medico', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='medicos.medicos')),
            ],
            options={
                'verbose_name': 'Médico',
                'verbose_name_plural': 'Médicos',
                'db_table': 'medicos',
            },
        ),
    ]
