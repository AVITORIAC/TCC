# Generated by Django 5.0.4 on 2024-05-14 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_autoavaliacao_options_alter_avaliacao_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='idTurma',
            field=models.IntegerField(default=0, null=True, verbose_name='Turma'),
        ),
    ]