# Generated by Django 4.1.5 on 2023-01-19 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='consulta',
            old_name='especial',
            new_name='especialidade_medica',
        ),
        migrations.RenameField(
            model_name='consulta',
            old_name='med',
            new_name='medico',
        ),
        migrations.AlterField(
            model_name='consulta',
            name='nomeC',
            field=models.CharField(max_length=100, verbose_name='Nome Cliente:'),
        ),
    ]
