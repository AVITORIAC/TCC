# Generated by Django 5.0.4 on 2024-05-14 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_criterio_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='autoavaliacao',
            options={'verbose_name': 'AutoAvaliação', 'verbose_name_plural': 'AutoAvaliações'},
        ),
        migrations.AlterModelOptions(
            name='avaliacao',
            options={'verbose_name': 'Avaliação', 'verbose_name_plural': 'Avaliações'},
        ),
        migrations.AlterModelOptions(
            name='criterio',
            options={'verbose_name': 'Critério', 'verbose_name_plural': 'Critérios'},
        ),
        migrations.AlterModelOptions(
            name='curso',
            options={'verbose_name': 'Curso', 'verbose_name_plural': 'Cursos'},
        ),
        migrations.AlterModelOptions(
            name='estado',
            options={'verbose_name': 'Estado', 'verbose_name_plural': 'Estados'},
        ),
        migrations.AlterModelOptions(
            name='nota_senai',
            options={'verbose_name': 'Nota Senai', 'verbose_name_plural': 'Notas Senai'},
        ),
        migrations.AlterModelOptions(
            name='observacao',
            options={'verbose_name': 'Observação', 'verbose_name_plural': 'Observações'},
        ),
        migrations.AlterModelOptions(
            name='semestre',
            options={'verbose_name': 'Semestre', 'verbose_name_plural': 'Semestres'},
        ),
        migrations.AlterModelOptions(
            name='tipo_avaliacao',
            options={'verbose_name': 'Tipo Avaliação', 'verbose_name_plural': 'Tipo Avaliações'},
        ),
        migrations.AlterModelOptions(
            name='turma',
            options={'verbose_name': 'Turma', 'verbose_name_plural': 'Turmas'},
        ),
        migrations.AlterField(
            model_name='usuario',
            name='idTurma',
            field=models.IntegerField(default=0, null=True, unique=True, verbose_name='Turma'),
        ),
    ]
