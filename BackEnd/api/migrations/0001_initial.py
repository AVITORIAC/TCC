import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
import fernet_fields.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Arquivo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('excel', models.FileField(upload_to='arquivo/')),
            ],
        ),
        migrations.CreateModel(
            name='Codigo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.IntegerField(default=1)),
                ('codigo', models.IntegerField()),
                ('data_geracao', models.DateTimeField(auto_now_add=True)),
                ('data_expiracao', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Ets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', fernet_fields.fields.EncryptedEmailField(max_length=254)),
                ('senha', fernet_fields.fields.EncryptedCharField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Recuperar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.IntegerField()),
                ('codigo', models.IntegerField()),
                ('senha', models.CharField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Semestre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_avaliacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('edv', fernet_fields.fields.EncryptedIntegerField(default=False, verbose_name='usuário apenas com seu número de edv')),
                ('email', fernet_fields.fields.EncryptedEmailField(max_length=254, verbose_name='Email')),
                ('nome', models.CharField(max_length=250, verbose_name='Nome Completo')),
                ('cargo', models.CharField(choices=[('aprendiz', 'Aprendiz'), ('instrutor', 'Instrutor'), ('gestor', 'Gestor'), ('administrador', 'Administrador')], default=False, max_length=20)),
                ('idTurma', models.IntegerField(default=0, null=True, verbose_name='Turma')),
                ('logado', models.BooleanField(default=True, verbose_name='Logado')),
                ('status', models.CharField(blank=True, choices=[('espera', 'Em espera'), ('aprovado', 'Aprovado'), ('rejeitado', 'Rejeitado')], default=None, max_length=20, null=True, verbose_name='Status do Cadastro')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
            },
        ),
        migrations.CreateModel(
            name='Nota_senai',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota', models.DecimalField(decimal_places=2, max_digits=2)),
                ('semestre', models.IntegerField()),
                ('idAprendiz', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Observacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.TextField()),
                ('idAprendiz', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('idEstado', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.estado')),
                ('idSemestre', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.semestre')),
            ],
        ),
        migrations.CreateModel(
            name='Criterio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=254)),
                ('descricao', models.TextField()),
                ('valido', models.BooleanField(default=True)),
                ('idCurso', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.curso')),
                ('idSemestre', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.semestre')),
                ('idTipo_avaliacao', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.tipo_avaliacao')),
            ],
        ),
        migrations.CreateModel(
            name='AutoAvaliacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota', models.DecimalField(decimal_places=2, max_digits=2)),
                ('idAprendiz', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('idCriterio', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.criterio')),
                ('idSemestre', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.semestre')),
            ],
        ),
        migrations.CreateModel(
            name='Turma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150, unique=True)),
                ('idCurso', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.curso')),
                ('idInstrutor', models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, related_name='turmas_instrutor', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Avaliacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota', models.DecimalField(decimal_places=2, max_digits=2)),
                ('idAprendiz', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('idCriterio', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.criterio')),
                ('idSemestre', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.semestre')),
                ('idTurma', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.turma')),
            ],
        ),
    ]
