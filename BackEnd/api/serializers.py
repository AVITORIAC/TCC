from rest_framework import serializers
from api.models import *
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password


class LoginSerializer(serializers.Serializer):
    """
        Classe para o login dos usuários, são definidos os campos e 
        depois esses campos são validados se o usuário existe e se estão corretos
    """
    edv = serializers.CharField(
        style={'input_type': 'username'},
        write_only=True,
        label="Usuário"
        )
    
    password = serializers.CharField(
        style={'input_type': 'password'},
        write_only=True,
        label="Senha"
        )

    def validate(self, attrs): # valida login
        edv = attrs.get('edv')
        password = attrs.get('password')

        if edv and password:
            try:
                # Verifica se o usuário existe no banco de dados
                user = Usuario.objects.get(edv=edv)
            except Usuario.DoesNotExist:
                return Response(data={"mensagem":"Usuário ou senha inválidos"}, status=status.HTTP_401_UNAUTHORIZED)

            # Verifica se a senha fornecida é correta para o usuário
            if not user.check_password(password):
                return Response(data={"mensagem":"Senha inválida"}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(data={"mensagem":"Os campos de usuário e senha são obrigatórios"}, status=status.HTTP_401_UNAUTHORIZED)

        attrs['user'] = user
        return attrs


class UsuarioSerializer(serializers.ModelSerializer):
    """
        Campos definidos são validados e salvos de acordo com o modelo do banco definido,
        e então o usuário é salvo quando cadastrado
    """
    password = serializers.CharField(
        max_length=20, 
        min_length=12, 
        style={'input_type': 'password'},
        write_only=True,
        label="Senha"
    )

    password_confirm = serializers.CharField(
        max_length=20, 
        min_length=12, 
        style={'input_type': 'password'},
        write_only=True,
        label="Confirme a senha"
    )

    class Meta():
        model = Usuario
        fields = ['edv', 'email', 'nome', 'cargo', 'idTurma', 'logado', 'status', 'password', 'password_confirm']
        read_only_fields = ['password', 'password_confirm']  # Define os campos como somente leitura

        
    def validate(self, data):
        password = data.get('password')
        password_confirm = data.get('password_confirm')

        if self.partial:  # Verifica se é uma atualização parcial
            if 'password' in data:
                del data['password']  # Remove o campo 'password' dos dados validados
            if 'password_confirm' in data:
                del data['password_confirm']  # Remove o campo 'password_confirm' dos dados validados

        if password and password != password_confirm:
            return Response(data={'password': "As senhas não são iguais"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

        return data

    def save(self, **kwargs):
        validated_data = self.validated_data
        password = validated_data.get('password')
        password_confirm = validated_data.pop('password_confirm', None)  # Remove password_confirm de validated_data

        if self.instance:  # Verifica se a instância existe
            if self.partial: # determina se a atualização dos dados é parcial 
                # FIXME No contexto de serialização em Django REST Framework, o atributo partial é um indicador que informa se a atualização dos dados é parcial ou completa.
                if 'password' in validated_data:
                    del validated_data['password']
                for key, value in validated_data.items():
                    setattr(self.instance, key, value) # função que define os valores dos campos do Usuario com base nos dados validados
            else:
                if password and password_confirm:
                    if password != password_confirm:
                        return Response(data={'password': "As senhas não são iguais"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
                    try:
                        validate_password(password, self.instance)
                    except ValidationError as e:
                        return serializers.ValidationError({'password': e.messages}, status.HTTP_401_UNAUTHORIZED) # mensagens de erro referentes a validação de senha
                    self.instance.save()
        else:
            # Cria uma nova instância do usuário se ela não existir, ou seja, criptografa a senha e salva a instância do usuário
            self.instance = Usuario(**validated_data)
            self.instance.set_password(password)
            self.instance.save()

        return self.instance


class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'


class TipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo_avaliacao
        fields = '__all__'



class EstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estado
        fields = '__all__'


class TurmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turma
        fields = '__all__'


class NotaSenaiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nota_senai
        fields = '__all__'


class SemestreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Semestre
        fields = '__all__'


class ObservacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Observacao
        fields = '__all__'


class CriterioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Criterio
        fields = '__all__'


class AvaliacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avaliacao
        fields = '__all__'


class AutoAvaliacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AutoAvaliacao
        fields = '__all__'


class ArquivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Arquivo
        fields = '__all__'
        

class CodigoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Codigo
        fields = '__all__'
        
        
class RecuperarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recuperar
        fields = '__all__'
        

class EtsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ets
        fields = '__all__'
