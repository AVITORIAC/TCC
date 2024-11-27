# Generated by Django 5.0.4 on 2024-05-17 12:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_usuario_idturma'),
        ('authtoken', '0004_alter_tokenproxy_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExpirandoToken',
            fields=[
                ('token_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='authtoken.token')),
                ('expira_token', models.DateTimeField(auto_now_add=True)),
            ],
            bases=('authtoken.token',),
        ),
        migrations.AddField(
            model_name='autoavaliacao',
            name='idTurma',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.PROTECT, to='api.turma'),
            preserve_default=False,
        ),
    ]
