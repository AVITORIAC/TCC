from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics
from django.db.models import Sum
from django.db.models import Avg
from api.models import *
from api.serializers import *
from meinung.permissions import *
import smtplib
import random
from django.utils import timezone
from datetime import timedelta
from cryptography.fernet import Fernet
from django.conf import settings
from django.contrib.auth.hashers import check_password


#FIXME-----VERIFICAR ERRO-----
fernet = Fernet(settings.FERNET_KEY)


class LoginView(generics.GenericAPIView):
    """
        View para o usuário poder se logar, juntamente com o envio do Token para autenticação
    """
    serializer_class = LoginSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [AllowAny]

    def post(self, request: Request):  # adiciona o login
        """
            Função para fazer login na plataforma, através de usuário e senha
        """
        
        usuario_edv = request.data['edv']
        usuario_senha = request.data['password']

        usuarios = Usuario.objects.all()

        for usuario in usuarios:
            usuario_edv_banco = usuario.decrypt_edv()
            if check_password(usuario_senha, usuario.password) and int(usuario_edv) == int(usuario_edv_banco) and usuario.status == "aprovado":                   
                if usuario.cargo == "aprendiz":
                    turma = usuario.idTurma
                    turma = Turma.objects.get(pk=turma)
                    curso = turma.idCurso
                    curso = curso.descricao
                else:
                    curso = ""
                
                token, created = Token.objects.get_or_create(user=usuario)
                response = {
                    "message": "Login feito com sucesso", 
                    "id": usuario.id,
                    "token": token.key, 
                    "cargo": usuario.cargo,
                    "curso": curso
                }
                return Response(data=response, status=200)
        return Response({"Erro": "Usuário ou senha incorretos."}, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(generics.GenericAPIView):
    """
        View para realizar o logout de um usuário autenticado.
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        # sobrescrevendo o método get_serializer para evitar erros
        return None 

    def post(self, request):
        # Recupera o token do cabeçalho de autorização
        token = request.headers.get('Authorization').split(' ')[1]

        # Procura o token no banco de dados
        try:
            auth_token = Token.objects.get(key=token)
        except Token.DoesNotExist:
            return Response({'detail': 'Token não encontrado'}, status=status.HTTP_404_NOT_FOUND)

        # Revoga o token (exclui-o do banco de dados)
        auth_token.delete()

        return Response({'detail': 'Logout feito com sucesso'}, status=status.HTTP_200_OK)


class UsuarioView(generics.GenericAPIView):
    """
        View de cadastro do usuário, 
        verifica o serializer e os campos definidos e se for válido,
        o usuário é cadastrado e salvo
    """
    queryset = Usuario.objects.all()
    serializer_class=UsuarioSerializer
    authentication_classes= [TokenAuthentication]
    permission_classes=[AllowAny]

    def post(self, request):
        serializer = UsuarioSerializer(data=request.data)
        if serializer.is_valid():
            cargo = serializer.validated_data.get('cargo')

            if cargo == 'administrador': # o status ja é aprovado caso seja admin
                serializer.validated_data['status'] = 'aprovado'
                serializer.save()
                return Response(data={"mensagem": "Cadastro aprovado com sucesso!"},status=status.HTTP_200_OK)
            
            elif cargo == 'aprendiz' or 'instrutor' or 'gestor': # define o status como espera se for aprendiz
                serializer.validated_data['status'] = 'em espera'
                serializer.save()
                return Response(data={"mensagem": "Cadastro em espera, aguarde ser aprovado"},status=status.HTTP_200_OK)

            else:
                return Response(data={"mensagem": "cadastro inválido, verifique se os campos estão corretos"}, status=status.HTTP_401_UNAUTHORIZED)
            
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UsuarioEdv(generics.RetrieveAPIView):
    """
    Classe para filtrar os usuários pelo EDV.
    """
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [AllowAny]
    
    def retrieve(self, request, edv=None):
        """
        Função que recebe o EDV e retorna as informações do usuário especificado.
        """
        try:
            # o edv é um dado criptografado, então é necessário pesquisar sem utilizar recursos reservados do django
            usuarios = Usuario.objects.all()
            for usuario in usuarios:
                if int(usuario.edv) == int(edv): 
                    serializer = self.serializer_class(usuario)
                    return Response({"id": usuario.pk}, status=200)  # Retornar os dados serializados
            return Response({"Erro": "Usuário não encontrado."}, status=404)  # Retornar erro se nenhum usuário for encontrado
        except Exception as e:
            return Response({"Erro": str(e)}, status=500)


class UsuarioUpdateView(generics.GenericAPIView):
    """
        Editar e aprovar usuários em espera
    """
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdministrador]
    lookup_field = 'pk'

    def get(self, request):
        """
            Função para exibir os aprendizes
        """
        queryset = Usuario.objects.all()
        serializer = UsuarioSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def get(self, request, pk=None):
        if pk:
            try:
                usuario = Usuario.objects.get(pk=pk)
                serializer = UsuarioSerializer(usuario)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Usuario.DoesNotExist:
                return Response(data={"mensagem": "Usuário não encontrado"}, status=status.HTTP_404_NOT_FOUND)
        else:
            queryset = Usuario.objects.all()
            serializer = UsuarioSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', True)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        if 'password' in serializer.validated_data:
            del serializer.validated_data['password']  # Remove o campo 'password' dos dados validados
        self.perform_update(serializer)
        instance.save()  
        return Response(serializer.data)
    
    def perform_update(self, serializer):
        serializer.save()
    
    def delete(self, request, pk):
        try:
            usuario = Usuario.objects.get(pk=pk)
        except Usuario.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        usuario.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# listas baseadas nos cargos
# é uma boa prática criar classes separadas para lidar com esses casos específicos

class AdminListView(generics.ListAPIView):
    """
        Lista que mostra o administrador cadastrado
    """
    serializer_class = UsuarioSerializer
    authentication_classes= [TokenAuthentication]
    permission_classes=[IsAuthenticated, IsAdministrador]

    def get_queryset(self):
        return Usuario.objects.filter(cargo='administrador')


class InstrutorListView(generics.ListAPIView):
    """
        Lista que mostra todos os instrutores cadastrados 
    """
    serializer_class = UsuarioSerializer
    authentication_classes= [TokenAuthentication]
    permission_classes=[IsAuthenticated, IsAdministrador]

    def get_queryset(self):
        return Usuario.objects.filter(cargo='instrutor')


class InstrutorEsperaListView(generics.ListAPIView):
    """
        Verifica os instrutores em que o cadastro está em espera
    """
    serializer_class = UsuarioSerializer
    authentication_classes= [TokenAuthentication]
    permission_classes=[IsAuthenticated, IsAdministrador]

    def get_queryset(self):
        return Usuario.objects.filter(cargo='instrutor', status='em espera') 


class InstrutorAprovadoListView(generics.ListAPIView):
    """
        Verifica os instrutores em que o cadastro está aprovado
    """
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    authentication_classes= [TokenAuthentication]
    permission_classes=[IsAuthenticated, IsAdministrador]

    def get_queryset(self):
        return Usuario.objects.filter(cargo='instrutor', status='aprovado')  


class GestorListView(generics.ListAPIView):
    """
        Lista que mostra o gestor cadastrado
    """
    serializer_class = UsuarioSerializer
    authentication_classes= [TokenAuthentication]
    permission_classes=[IsAuthenticated, IsAdministrador]

    def get_queryset(self):
        return Usuario.objects.filter(cargo='gestor')


class GestorEsperaListView(generics.ListAPIView):
    """
        Verifica o gestor em que o cadastro está em espera
    """
    serializer_class = UsuarioSerializer
    authentication_classes= [TokenAuthentication]
    permission_classes=[IsAuthenticated, IsAdministrador]

    def get_queryset(self):
        return Usuario.objects.filter(cargo='gestor', status='em espera') 


class GestorAprovadoListView(generics.ListAPIView):
    """
        Verifica o gestor em que o cadastro está aprovado
    """
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    authentication_classes= [TokenAuthentication]
    permission_classes=[IsAuthenticated, IsAdministrador]

    def get_queryset(self):
        return Usuario.objects.filter(cargo='gestor', status='aprovado')  


class AllAprendizListView(generics.ListAPIView):
    """
        Lista todos os aprendizes cadastrados
    """
    serializer_class = UsuarioSerializer
    authentication_classes= [TokenAuthentication]
    permission_classes=[IsAuthenticated, IsAdministrador]

    def get_queryset(self):
        return Usuario.objects.filter(cargo='aprendiz') 



class AprendizEsperaListView(generics.ListAPIView):
    """
        Verifica os aprendizes em que o cadastro está em espera
    """
    serializer_class = UsuarioSerializer
    authentication_classes= [TokenAuthentication]
    permission_classes=[IsAuthenticated, IsAdministrador]

    def get_queryset(self):
        return Usuario.objects.filter(cargo='aprendiz', status='em espera') 


class AprendizAprovadoListView(generics.ListAPIView):
    """
        Verifica os aprendizes em que o cadastro está aprovado
    """
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    authentication_classes= [TokenAuthentication]
    permission_classes=[IsAuthenticated, IsAdministrador]

    def get_queryset(self):
        return Usuario.objects.filter(cargo='aprendiz', status='aprovado')  


class RendimentoAprendizView(generics.GenericAPIView):
    """
        rendimento do aprendiz, em que ele pode selecionar os semestres para comparação
    """
    serializer_class = AutoAvaliacaoSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAprendiz]

    def get(self, request, id_semestre1, id_semestre2, format=None):
        semestre1 = AutoAvaliacao.objects.filter(idSemestre_id=id_semestre1)
        semestre2 = AutoAvaliacao.objects.filter(idSemestre_id=id_semestre2)

        if semestre1 and semestre2 is not None:
            semestre1_serializer = AutoAvaliacaoSerializer(semestre1, many=True).data
            semestre2_serializer = AutoAvaliacaoSerializer(semestre2, many=True).data

            return Response({
                'notas_semestre1': semestre1_serializer,
                'notas_semestre2': semestre2_serializer,
            }, status=status.HTTP_200_OK)

        else:
            return Response({"Erro": "Todos os campos devem ser preenchidos"}, status=status.HTTP_401_UNAUTHORIZED)



class CompararTurmasView(generics.GenericAPIView): 
    """
        View para comparar médias das turmas
    """
    serializer_class = AvaliacaoSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsGestor]

    def get(self, request, turma1_id, turma2_id, semestre_id, format=None):
        # Calcula a média das notas dos aprendizes da primeira turma
        media_turma1 = self.calcular_media_turma(turma1_id, semestre_id)
        
        # Calcula a média das notas dos aprendizes da segunda turma
        media_turma2 = self.calcular_media_turma(turma2_id, semestre_id)

        return Response({
            'media_turma1': media_turma1,
            'media_turma2': media_turma2
        }, status=status.HTTP_200_OK)

    def calcular_media_turma(self, turma_id, semestre_id):
        # Filtra as avaliações dos aprendizes da turma no semestre específico
        avaliacoes = Avaliacao.objects.filter(idTurma=turma_id, idSemestre=semestre_id)

        # Calcula a média das notas dos aprendizes da turma
        media_turma = avaliacoes.aggregate(media=Avg('nota'))['media']
        # Avg é uma função de agregação do django, permite calcular a média de um campo numérico em um conjunto de objetos de modelo

        if media_turma is None:
            media_turma = 0  # Define a média como 0 se não houver avaliações
        return media_turma


class CompararAprendizesView(generics.GenericAPIView):
    """
        Exibe as notas de um aluno e quantidade de observações positivas e de melhorias, 
        com filtros por tipo de critério, critério, semestre e comparar dois aprendizes.
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsInstrutor]

    def get(self, request, id_aprendiz1, id_semestre, id_criterio=None, id_tipo_avaliacao=None, id_aprendiz2=None, format=None):
        # Filtra as avaliações do aprendiz 1 no semestre específico
        avaliacoes_aprendiz1 = Avaliacao.objects.filter(idAprendiz_id=id_aprendiz1, idSemestre_id=id_semestre)
        
        # Filtra as observações do aprendiz 1 no semestre específico
        observacoes_aprendiz1 = Observacao.objects.filter(idAprendiz_id=id_aprendiz1, idSemestre_id=id_semestre)

        # Filtra os critérios pelo tipo de avaliação, se fornecido
        if id_tipo_avaliacao is not None:
            criterios = Criterio.objects.filter(idSemestre_id=id_semestre, idTipo_avaliacao_id=id_tipo_avaliacao)
        else:
            criterios = Criterio.objects.filter(idSemestre_id=id_semestre)
        
        # Filtra os critérios pelo ID do critério, se fornecido
        if id_criterio is not None:
            criterios = criterios.filter(id=id_criterio)

        # Serializa os dados do aprendiz 1
        avaliacoes_aprendiz1_serializer = AvaliacaoSerializer(avaliacoes_aprendiz1, many=True).data
        observacoes_aprendiz1_serializer = ObservacaoSerializer(observacoes_aprendiz1, many=True).data
        criterios_serializer = CriterioSerializer(criterios, many=True).data

        # Conta a quantidade de observações positivas e de melhorias para o aprendiz 1
        qtd_observacoes_positivas_aprendiz1 = Observacao.objects.filter(idAprendiz_id=id_aprendiz1, idEstado=1).count()
        qtd_observacoes_melhorias_aprendiz1 = Observacao.objects.filter(idAprendiz_id=id_aprendiz1, idEstado=2).count()

        # Se o ID do aprendiz 2 for fornecido, realiza as filtragens e contagens correspondentes
        if id_aprendiz2 is not None:

            avaliacoes_aprendiz2 = Avaliacao.objects.filter(idAprendiz_id=id_aprendiz2, idSemestre_id=id_semestre)
            
            observacoes_aprendiz2 = Observacao.objects.filter(idAprendiz_id=id_aprendiz2, idSemestre_id=id_semestre)

            avaliacoes_aprendiz2_serializer = AvaliacaoSerializer(avaliacoes_aprendiz2, many=True).data
            observacoes_aprendiz2_serializer = ObservacaoSerializer(observacoes_aprendiz2, many=True).data

            qtd_observacoes_positivas_aprendiz2 = Observacao.objects.filter(idAprendiz_id=id_aprendiz2, idEstado=1).count()
            qtd_observacoes_melhorias_aprendiz2 = Observacao.objects.filter(idAprendiz_id=id_aprendiz2, idEstado=2).count()

        # caso o campo do aprendiz 2 estiver vazio, retorna uma mensagem de erro
        elif id_aprendiz2 == 0 or None:
            return Response(data={"Erro": "Os campos não devem estar vazios"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

        else:
            return Response(serializers.errors, status=status.HTTP_401_UNAUTHORIZED)

        # Retorna os dados serializados
        return Response({
            'avaliacoes_aprendiz1': avaliacoes_aprendiz1_serializer,
            'avaliacoes_aprendiz2': avaliacoes_aprendiz2_serializer,
            'observacoes_aprendiz1': observacoes_aprendiz1_serializer,
            'observacoes_aprendiz2': observacoes_aprendiz2_serializer,
            'qtd_observacoes_positivas_aprendiz1': qtd_observacoes_positivas_aprendiz1,
            'qtd_observacoes_melhorias_aprendiz1': qtd_observacoes_melhorias_aprendiz1,
            'qtd_observacoes_positivas_aprendiz2': qtd_observacoes_positivas_aprendiz2,
            'qtd_observacoes_melhorias_aprendiz2': qtd_observacoes_melhorias_aprendiz2,
            'criterios': criterios_serializer
        }, status=status.HTTP_200_OK)


class MediaView(generics.GenericAPIView): 
    """
        Função para calcular e exibir a nota final da avaliação do aprendiz (filtrando por semestre também)
    """
    queryset = Avaliacao.objects.all()
    serializer_class= AvaliacaoSerializer
    authentication_classes= [TokenAuthentication]
    permission_classes=[IsAuthenticated, IsInstrutor]

    def get(self, request, idAprendiz, idSemestre, idTurma, format=None):
        # Filtra as avaliações do aprendiz no semestre específico
        avaliacoes = Avaliacao.objects.filter(idTurma=idTurma, idAprendiz=idAprendiz, idSemestre=idSemestre)

        # Soma as notas dos critérios
        nota_final = avaliacoes.aggregate(total=Sum('nota'))['total']
        # função de agregação fornecida pelo Django que permite calcular a soma de um campo numérico em um conjunto de objetos de modelo

        # Se nenhuma avaliação for encontrada, define como 0
        if nota_final is None:
            nota_final = 0

        # Retorna a nota final 
        return Response({'nota_final': nota_final}, status=status.HTTP_200_OK)


class DetalhesAvaliacaoView(generics.GenericAPIView):
    """
        Exibe as notas do aprendiz na avaliação, os critérios e as observações (filtrados por semestre).
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsInstrutor]

    def get(self, request, idAprendiz, idSemestre, format=None):
        # Filtra as avaliações do aprendiz no semestre específico
        avaliacoes = Avaliacao.objects.filter(idAprendiz_id=idAprendiz, idSemestre_id=idSemestre)
        observacoes = Observacao.objects.filter(idAprendiz_id=idAprendiz, idSemestre_id=idSemestre)
        criterios = Criterio.objects.filter(idSemestre_id=idSemestre)

        # Serializa os dados
        avaliacoes_serializer = AvaliacaoSerializer(avaliacoes, many=True).data
        observacoes_serializer = ObservacaoSerializer(observacoes, many=True).data
        qtd_observacoes_positivas_aprendiz = Observacao.objects.filter(idAprendiz_id=idAprendiz, idEstado=1).count()
        qtd_observacoes_melhorias_aprendiz = Observacao.objects.filter(idAprendiz_id=idAprendiz, idEstado=2).count()
        criterios_serializer = CriterioSerializer(criterios, many=True).data

        # Retorna os dados serializados 
        return Response({
            'avaliacoes': avaliacoes_serializer,
            'observacoes': observacoes_serializer,
            'observações_positivas': qtd_observacoes_positivas_aprendiz,
            'observações_melhorias': qtd_observacoes_melhorias_aprendiz,
            'criterios': criterios_serializer
        }, status=status.HTTP_200_OK)


class FeedbackView(generics.GenericAPIView):
    """
        View para o Feedback,
        exibe a nota final da avaliação (após o consenso entre instrutor e aprendiz) do aprendiz 
        e os detalhes da avaliação.
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsInstrutor]

    def get(self, request, idAprendiz, idSemestre, idTurma, format=None):
        # Chama a função para calcular a média da avaliação do aprendiz
        media_view = MediaView()
        nota_final = media_view.get(request, idAprendiz, idSemestre, idTurma).data

        # Chama a função para exibir os detalhes da avaliação do aprendiz
        detalhes_avaliacao_view = DetalhesAvaliacaoView()
        detalhes_avaliacao = detalhes_avaliacao_view.get(request, idAprendiz, idSemestre).data

        # Retorna a nota final e os detalhes da avaliação
        return Response({
            'nota_final': nota_final,
            'detalhes_avaliacao': detalhes_avaliacao
        }, status=status.HTTP_200_OK)


class CodigoView(generics.GenericAPIView):
    """
        Classe para gerar o código de recuperação de senha e enviar por e-mail.
    """
    serializer_class = CodigoSerializer
    permission_classes=[AllowAny]    
    
    def get(self, request):
        """
            Função que retorna o último código requerido por um determinado usuário.
        """
        try:
            usuario = self.request.query_params.get('pk') # pegando o id passado na url
            if usuario is not None: # se for passado um usuário
                queryset = Codigo.objects.filter(usuario=usuario).last() # faz uma busca do usuário e o último registro dele no banco de dados
                if queryset is not None:
                    serializer = CodigoSerializer(queryset) 
                    return Response(serializer.data, status=status.HTTP_200_OK)
                else:                   
                    return Response({"Erro": "usuário não encontrado!"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"Erro": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                
    def post(self, request):
        """
            Função para gerar o código e enviar pelo e-mail para o usuário.
        """
        serializer = self.serializer_class(data=request.data)
        
        try:   
            # adicionando as datas e o código que foi gerado para salvar no banco de dados     
            codigo_gerado = random.randint(100000, 999999)
            serializer = CodigoSerializer(data={
                'codigo': codigo_gerado,
                'data_geracao': timezone.now(),
                'data_expiracao': timezone.now() + timedelta(minutes=10),
                'usuario': request.data['usuario'],
            })
            
            # usuário que está pedindo o código de recuperação de senha
            usuario = Usuario.objects.get(pk=request.data['usuario'])
            email_usuario = usuario.email
            
            # usuário que envia o e-mail de recuperação de senha
            usuario_login = Ets.objects.last()
            
            if serializer.is_valid():
                serializer.save()
                enviar_email(usuario_login.email, email_usuario, codigo_gerado, usuario_login.email, usuario_login.senha)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"Erro:": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# de - quem envia o email
# para - quem recebe o email
# codigo - codigo de recuperação gerado
# email - email de quem vai logar para enviar o email
# senha - senha de quem vai logar para enviar o email
def enviar_email(de, para, codigo, email, senha):
    """
        Função para criar e enviar o e-mail.
    """
    try:
        FROM = de
        TO = para
        SUBJECT = 'Meinung - Código de recuperação'
        TEXT = f"O código para alteração da senha é {codigo} e expira em 10 minutos."
        mensagem = f'Subject: {SUBJECT}\n\n{TEXT}\n\n\nEquipe Meinung :)'
        mensagemUtf = mensagem.encode('utf-8')        
        with smtplib.SMTP('rb-smtp-auth.rbesz01.com', 25) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()
            smtp.login(email, senha)
            smtp.sendmail(FROM, TO, mensagemUtf)
        smtp.quit()
    except Exception as e:
        print(e)
        
        
class RecuperarView(generics.GenericAPIView):
    """
        Classe para a recuperação da senha.
    """
    serializer_class = RecuperarSerializer
    permission_classes = [AllowAny]
    
    def post(self, request):
        """
            Função para verificar o código e alterar a senha.
        """
        serializer = self.serializer_class(data=request.data)
        
        # try:
        codigo_recebido = request.data['codigo']
        usuario = request.data['usuario']
        nova_senha = request.data['senha']
        codigo_armazenado = Codigo.objects.filter(usuario=usuario).last() # pegando o último objeto armazenado com esse usuário
        
        print(f'Codigo recebido: {codigo_recebido}')
        print(f'Codigo armazenado: {codigo_armazenado.codigo}')
        
        if int(codigo_recebido) == int(codigo_armazenado.codigo) and timezone.now() < codigo_armazenado.data_expiracao:
            usuario_editar = Usuario.objects.get(pk=usuario) # procurando o usuário pelo id
            registro_editado = {
                'password': nova_senha,
                'password_confirm': nova_senha
            }
            serializer = UsuarioSerializer(usuario_editar, data=registro_editado, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"Sucesso": "Senha alterada com sucesso!"}, status=status.HTTP_200_OK)                
        else:
            return Response({"Erro": "Esse código não exite ou está expirado."}, status=status.HTTP_400_BAD_REQUEST)
        # except Exception as e:
        #     return Response({"Erro": str(e)}, status=500)
            
            
            
class EtsView(generics.GenericAPIView):
    """
        Classe para alterar o usuário que envia os e-mails de recuperação de senha.
    """
    serializer_class = EtsSerializer
    permission_classes = [AllowAny]
    queryset = Ets.objects.all()
    
    def get(self, request):
        """
            Função para apresentar o usuário cadastrado para enviar o e-mail.
        """
        try:
            queryset = Ets.objects.all()
            serializer = EtsSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"Erro": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def post(self, request):
        """
            Função para cadastrar o usuário.
        """                
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request):
        """
            Função para alterar o usuário que envia o email de recuperação da senha.
        """
        try:
            queryset = Ets.objects.all()
            pk = request.query_params.get('pk') # recebe o id do usuário
            registro = queryset.get(pk=pk) # encontra o registro no banco de dados
        except Ets.DoesNotExist:
            return Response("Erro", "usuário não encontrado!", status=status.HTTP_404_NOT_FOUND)
        
        serializer = self.serializer_class(registro, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)
