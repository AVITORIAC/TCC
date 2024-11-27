#Criação das tabelas no banco de dados
from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from .managers import UserManager
from django.contrib.auth.models import Group, Permission
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from fernet_fields.fields import EncryptedEmailField, EncryptedIntegerField, EncryptedCharField
from meinung.roles import *
from django.utils import timezone
from rest_framework.authtoken.models import Token
from rolepermissions.checkers import has_role


class ExpirandoToken(Token):
    """
        Modelo personalizado para expiração do token 
    """
    expira_token = models.DateTimeField(auto_now_add=True)  # Adiciona um campo de data/hora para armazenar a expiração do token

    def foi_expiradp(self):
        """
            Método para verificar se o token expirou
        """
        # Define o tempo de expiração para 5 segundos após a criação do token
        tempo_expiracao = self.expira_token + timezone.timedelta(seconds=5)
        return timezone.now() > self.tempo_expiracao  #  Verifica se o token expirou comparando a data/hora atual com a data/hora de expiração do token


class Curso(models.Model):
    """
        Model com o nome de cada curso.
    """
    descricao = models.CharField(max_length=255, null=False) # nome do curso

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"
    
    def __str__(self):
        return self.descricao
    
    
class Tipo_avaliacao(models.Model):
    """
        Model com os tipo de avaliação, que pode ser auto avaliação (realizada pelo aprendiz) 
        e avaliação (realizada pelo instrutor)
    """
    descricao = models.CharField(max_length=20, null=False)

    class Meta:
        verbose_name = "Tipo Avaliação"
        verbose_name_plural = "Tipo Avaliações"

    def __str__(self):
        return self.descricao
    
    
class Estado(models.Model):
    """
        Estado da nota que foi atribuida a um aprendiz, se ela é positiva ou de melhoria.
    """
    descricao = models.CharField(max_length=10, null=False)

    class Meta:
        verbose_name = "Estado"
        verbose_name_plural = "Estados"
    
    def __str__(self):
        return self.descricao


class Usuario(AbstractUser, PermissionsMixin):
    """
        Classe abstrata para o usuário com os campos padrões de cadastro
    """

    CARGO_CHOICES = [
        ('aprendiz', "Aprendiz"),
        ('instrutor', "Instrutor"),
        ('gestor', "Gestor"),
        ('administrador', "Administrador")
    ]

    STATUS_CHOICES = [
        ('espera', 'Em espera'),
        ('aprovado', 'Aprovado'),
        ('rejeitado', 'Rejeitado'),
    ]

    edv = EncryptedIntegerField(null=False, verbose_name="usuário apenas com seu número de edv", default=False)
    email = EncryptedEmailField(max_length=254, null=False, verbose_name="Email")
    nome = models.CharField(max_length=250, null=False, verbose_name="Nome Completo")
    cargo = models.CharField(max_length=20, null=False, choices=CARGO_CHOICES, default=False)
    idTurma = models.IntegerField(null=True, verbose_name="Turma", default=0)
    logado = models.BooleanField(null=False, verbose_name="Logado") #FIXME verificar se precisa ainda
    status = models.CharField(max_length=20, null=True, choices=STATUS_CHOICES, verbose_name="Status do Cadastro", default=None, blank=True)

    USERNAME_FIELDS = ['edv']
    REQUIRED_FIELDS = ['email', 'logado']

    objects = UserManager()

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"


    def check_user_role(self, role):
        """
            Verifica se o usuário pertence a um determinado grupo de permissões, 
            com base no nome do grupo
        """
        return self.groups.filter(name=role).exists()


    def save(self, *args, **kwargs):
        """
            Salva os usuários, verifica o cargo do usuário e atribui o grupo e as permissões correspondentes
        """
        if not self.username:
            self.username = make_password(str(self.edv))  # Criptografa o edv para usar como username

        super().save(*args, **kwargs)

        if self.cargo:
            group_name = self.cargo.capitalize()
            group, created = Group.objects.get_or_create(name=group_name)

            if group_name in permission_role_mapping:
                role_class = permission_role_mapping[group_name]
                permissions = Permission.objects.filter(codename__in=role_class.available_permissions.keys())
                group.permissions.set(permissions)
                self.groups.add(group)
            else:
                return Response(data={"mensagem": "Verifique se esse cargo existe"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(data={"erro": "Tente Novamente"}, status=status.HTTP_401_UNAUTHORIZED)

    def get_permissions(self):
        """
            Esta função retorna todas as permissões do usuário 
            baseado nos grupos e roles aos quais o usuário pertence.
        """
        permissions = set()

        for group in self.groups.all():
            permissions.update(group.permissions.values_list('codename', flat=True))

        for role_name, role_class in permission_role_mapping.items():
            if has_role(self, role_class):
                permissions.update(role_class.available_permissions.keys())

        return permissions
    
    def decrypt_edv(self):
        encrypted_field = EncryptedIntegerField()
        return encrypted_field.get_prep_value(self.edv)

    def __str__(self):
        return self.nome


class Turma(models.Model):
    """
        Turmas cadastradas na ETS em que consta o padrinho/madrinha da turma, o curso e o nome.
    """
    nome = models.CharField(unique=True, max_length=150)
    idInstrutor = models.ForeignKey(Usuario, null=False, on_delete=models.PROTECT, default='', related_name='turmas_instrutor')
    idCurso = models.ForeignKey(Curso, null=False, on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Turma"
        verbose_name_plural = "Turmas"
    
    def __str__(self):
        return self.nome


class Nota_senai(models.Model):
    """
        Nota do SENAI já com a média calculada entre as notas nas diciplinas e a frequência nas aulas.
    """
    idAprendiz = models.ForeignKey(Usuario, null=False, on_delete=models.PROTECT)
    nota = models.DecimalField(max_digits=2, decimal_places=1, null=False)
    semestre = models.IntegerField(null=False)

    class Meta:
        verbose_name = "Nota Senai"
        verbose_name_plural = "Notas Senai"
    
    def __str__(self):
        return f"{self.idAprendiz}" 


class Semestre(models.Model):
    """
        Semestres que os cursos possuem.
    """
    descricao = models.CharField(max_length=50, null=False)

    class Meta:
        verbose_name = "Semestre"
        verbose_name_plural = "Semestres"
   
    def __str__(self):
        return self.descricao


class Observacao(models.Model):
    """
        Observações que os instrutores fazem dos aprendizes durante o semestre.
    """
    idAprendiz = models.ForeignKey(Usuario, null=False, on_delete=models.PROTECT)
    descricao = models.TextField(null=False)
    idEstado = models.ForeignKey(Estado, null=False, on_delete=models.PROTECT)
    idSemestre = models.ForeignKey(Semestre, null=False, on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Observação"
        verbose_name_plural = "Observações"
    
    def __str__(self):
        return f"{self.idAprendiz}"
    

class Criterio(models.Model):
    """
        Critérios utilizados para avaliar os aprendizes.
    """

    id = models.AutoField(primary_key=True, editable=False) # campo adicionado para o filtro de rendimento, não irá aparecer na hora de cadastrar
    nome = models.CharField(max_length=254, null=False)
    descricao = models.TextField(null=False)
    idCurso = models.ForeignKey(Curso, null=False, on_delete=models.PROTECT)
    idSemestre = models.ForeignKey(Semestre, null=False, on_delete=models.PROTECT)
    idTipo_avaliacao = models.ForeignKey(Tipo_avaliacao, null=False, on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Critério"
        verbose_name_plural = "Critérios"
    
    def __str__(self):
        return self.nome
    

class Avaliacao(models.Model):
    """
        Contem as notas da auto avaliação do aprendiz.
    """
    idTurma = models.ForeignKey(Turma, null=False, on_delete=models.PROTECT)
    idAprendiz = models.ForeignKey(Usuario, null=False, on_delete=models.PROTECT)
    idSemestre = models.ForeignKey(Semestre, null=False, on_delete=models.PROTECT)
    idCriterio = models.ForeignKey(Criterio, null=False, on_delete=models.PROTECT)
    nota = models.DecimalField(max_digits=2, decimal_places=1, null=False)

    class Meta:
        verbose_name = "Avaliação"
        verbose_name_plural = "Avaliações"
    
    def __str__(self):
        return f"{self.idAprendiz}"


class AutoAvaliacao(models.Model):
    """
    Auto Avalição realizada pelo aprendiz
    """
    idAprendiz = models.ForeignKey(Usuario, null=False, on_delete=models.PROTECT)
    idTurma = models.ForeignKey(Turma, null=False, on_delete=models.PROTECT)
    idSemestre = models.ForeignKey(Semestre, null=False, on_delete=models.PROTECT)
    idCriterio = models.ForeignKey(Criterio, null=False, on_delete=models.PROTECT)
    nota = models.DecimalField(max_digits=2, decimal_places=1, null=False)

    class Meta:
        verbose_name = "AutoAvaliação"
        verbose_name_plural = "AutoAvaliações"

    def __str__(self):
        return f"{self.idAprendiz}"
    

class Arquivo(models.Model):
    """
        Classe para armazenar temporariamente o arquivo excel com as notas do SENAI.
    """
    excel = models.FileField(upload_to='arquivo/')

    
class Codigo(models.Model):
    """
        Model para armazenar os códigos que são gerados para recuperar a senha.
    """
    usuario = models.IntegerField(null=False, default=1)
    codigo = models.IntegerField(null=False)
    data_geracao = models.DateTimeField(auto_now_add=True)
    data_expiracao = models.DateTimeField(null=False)
    
    def __str__(self):
        return self.usuario
    
    
class Recuperar(models.Model):
    """
        Model para receber os dados e alterar a senha do usuário.
    """
    usuario = models.IntegerField(null=False)
    codigo = models.IntegerField(null=False)
    senha = models.CharField(max_length=254, null=False)
    
    def __str__(self):
        return self.usuario
    
class Ets(models.Model):
    """
        Model que armazena o email e a senha do usuário que envia o e-mail de recuperação.
    """
    email = EncryptedEmailField(null=False)
    senha = EncryptedCharField(max_length=254, null=False)
    
    def __str__(self):
        return self.email