from rest_framework import viewsets
from api.serializers import *
from api.models import *
from meinung.permissions import *
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework import status
import pandas as pd  # importando a biblioteca de análise do excel
import os
from django_filters.rest_framework import DjangoFilterBackend 
from .filters import *
from rest_framework.decorators import action
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


def carregar_notas():
    """
        Função para carregar as notas do excel para o banco de dados.
    """
    # local onde as informações serão armazenadas
    serializer_class = NotaSenaiSerializer
    queryset = Nota_senai.objects.all()
    
    valores_separados = {}
    valores_media = {}

    tabela = pd.read_excel('uploads/arquivo/Notas.xlsx')  # caminho silmples porque o arquivo está na mesma pasta

    qtd_linhas = tabela['Nome'].count()  # quantidade de registros da planilha

    # percorrer todas as linhas da tabela
    for i in range(qtd_linhas):
        # se o nome dessa linha estiver dentro do dicionário
        if tabela['Nome'].loc[i] in valores_separados:
            # a chave com o nome dessa linha será somado a nota e a frequencia com o que já está armazenado
            valores_separados[f'{tabela["Nome"].loc[i]}'][0] = valores_separados[f'{tabela["Nome"].loc[i]}'][0] + tabela['Nota Final'].loc[i] # somando as notas
            valores_separados[f'{tabela["Nome"].loc[i]}'][1] = valores_separados[f'{tabela["Nome"].loc[i]}'][1] + tabela['Frequência'].loc[i] # somando a frequência
            valores_separados[f'{tabela["Nome"].loc[i]}'][2] = valores_separados[f'{tabela["Nome"].loc[i]}'][2] + 1 # somando a quantidade de materias
        else:
            # caso seja um novo nome é adicionado no dicionário com a nota final, a frequência e o semestre em lista
            valores_separados[f'{tabela["Nome"].loc[i]}'] = [tabela['Nota Final'].loc[i], tabela['Frequência'].loc[i], 1, tabela['Turma'].loc[i]]

    # calculo da média
    for chave, valores in valores_separados.items():
        media_nota = valores[0] / valores[2] # calculo da média da nota
        media_frequencia = valores[1] / valores[2] # calculo da média da frequência
        media_total = (media_nota + media_frequencia) / 2 # média da frequencia e da nota
        media_total = (5 * media_total) / 100
        media_total = round(media_total, 1)
        
        # armazenando o semestre e pegando somente o primeiro número
        semestre = valores_separados[chave][3]
        semestre = semestre[0]
        
        valores_media[chave] = [media_total, semestre] # adicionando no dicionário as médias e o semestre

    print(valores_media.items())
    for chave, valores in valores_media.items():
        # separando as informações do excel
        nome_aprendiz = chave
        nota_aprendiz = valores[0]
        semestre_aprendiz = valores[1]
        
        try:            
            aprendiz = Usuario.objects.get(nome=nome_aprendiz)
            
            # salvando os dados das notas do aprendiz
            dados = {
                'idAprendiz': aprendiz.id,
                'nota': nota_aprendiz,
                'semestre': semestre_aprendiz
            }
            
            _serializer = serializer_class(data=dados)
            
            if _serializer.is_valid():
                _serializer.save()
            else:
                print(_serializer.errors)
            
        except Usuario.DoesNotExist: # caso o aprendiz não seja encontrado
            print("Erro: Aprendiz não encontrado")
        
        except Exception as e: # tratamento para outros erros
            print(str(e))


class ArquivoViewSet(viewsets.ModelViewSet):
    """
        Classe para tratar o excel e inserir as notas dos aprendizes no banco de dados.
    """
    serializer_class = ArquivoSerializer
    queryset = Arquivo.objects.all()
    permission_classes = [AllowAny]
    
    def create(self, request, *args, **kwargs):
        """
            Função para enviar as notas para o banco de dados.
        """
        _serializer = self.serializer_class(data=request.data)
        if _serializer.is_valid():
            _serializer.save() # salvando o arquivo
            carregar_notas() # carregando e tratando os dados para o banco
            # apagando o arquivo que já foi processado
            if os.path.exists('uploads/arquivo/Notas.xlsx'):
                os.remove('uploads/arquivo/Notas.xlsx')
                print('Arquivo removido')
            else:
                'o caminho do arquivo não existe'
            return Response(data=_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CursoViewSet(viewsets.ModelViewSet):
    """
        Função para cadastro dos cursos
    """
    queryset = Curso.objects.all()
    serializer_class=CursoSerializer
    authentication_classes= [TokenAuthentication]
    permission_classes=[IsAuthenticated, IsAdministrador]

    # Implementação da função list para listar todos os objetos
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()  # Obtém a lista de objetos
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # Implementação da função retrieve para recuperar um objeto pelo ID
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()  # Obtém a instância do objeto com base no ID
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
    
    # Implementação da função destroy para excluir pelo ID
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()  
        self.perform_destroy(instance)
        return Response(status=status.HTTP_200_OK)
    
    # Implementação da função update para atualizar um objeto existente
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()  
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)


class TurmaViewSet(viewsets.ModelViewSet):
    """
        Função para cadastro das turmas de cada curso
    """
    queryset = Turma.objects.all()
    serializer_class=TurmaSerializer
    authentication_classes= [TokenAuthentication]
    permission_classes=[IsAuthenticated, IsAdministrador]

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset() 
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            turma = Turma.objects.get(pk=pk)
            serializer = TurmaSerializer(turma)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Turma.DoesNotExist:
            return Response(data={"mensagem": "Turma não encontrado"}, status=status.HTTP_404_NOT_FOUND)

    def create(self, request, *args, **kwargs):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()  
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)


class TipoViewSet(viewsets.ModelViewSet):
    """
        Função para cadastro dos tipos de avaliações
    """
    queryset = Tipo_avaliacao.objects.all()
    serializer_class=TipoSerializer
    authentication_classes= [TokenAuthentication]
    permission_classes=[IsAuthenticated, IsAdministrador]

    def create(self, request, *args, **kwargs):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NotaSenaiViewSet(viewsets.ModelViewSet): 
    """
        Função para as notas do senai
    """
    queryset = Nota_senai.objects.all
    serializer_class=NotaSenaiSerializer
    authentication_classes= [TokenAuthentication]
    permission_classes=[IsAuthenticated, IsInstrutor]

    def create(self, request, *args, **kwargs):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SemestreViewSet(viewsets.ModelViewSet): 
    """
        Função para cadastro dos semestres
    """
    queryset= Semestre.objects.all()
    serializer_class=SemestreSerializer
    authentication_classes= [TokenAuthentication]
    permission_classes=[IsAuthenticated, IsAdministrador] 

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ObservacaoViewSet(viewsets.ModelViewSet): 
    """
        Função para observações feitas dos aprendizes 
    """
    queryset = Observacao.objects.all()
    serializer_class=ObservacaoSerializer
    authentication_classes= [TokenAuthentication]
    permission_classes=[IsAuthenticated, IsInstrutor]

    def create(self, request, *args, **kwargs):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EstadoViewSet(viewsets.ModelViewSet):
    """"
        Função para cadastro do estado das observações (positivo ou de melhoria)
    """
   
    queryset = Estado.objects.all()
    serializer_class = EstadoSerializer
    authentication_classes= [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsInstrutor]

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST) 


class CriterioViewSet(viewsets.ModelViewSet):
    """
        Função para cadastro dos critérios
    """
    queryset = Criterio.objects.all()
    serializer_class = CriterioSerializer
    authentication_classes= [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdministrador]

    def get(self, request):
        """
            Função que lista todos os critérios e pesquisa os critérios.
        """
        serializer = CriterioSerializer(self.queryset, many=True)
        nome_criterio = self.request.query_params.get('criterio')
        if nome_criterio is not None:
            self.queryset = self.queryset.filter(nome__icontains=nome_criterio)
            serializer = CriterioSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwarg):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

    def partial_update(self, request, pk=None):
        """
            Função para editar um critério já cadastrado, podendo desativá-lo quando não é mais usado.
        """
        try:
            registro = self.queryset.get(pk=pk)
        except Criterio.DoesNotExist:
            return Response({"Erro": "Critério não encontrado!"}, status=404)
        
        serializer = self.serializer_class(registro, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)


class CriterioFiltroViewSet(viewsets.ModelViewSet):
    """
        Função para rota de rendimento na tela do instrutor
        (filtro por tipo de critério e critério)
    """
    queryset = Criterio.objects.all()
    serializer_class = CriterioSerializer
    authentication_classes= [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsInstrutor]
    filter_backends = [DjangoFilterBackend] # responsável por aplicar os filtros definidos 
    filterset_class = CriterioFilter # especifica a classe de filtro a ser usada

    @action(detail=False, methods=['get']) # não está associada a um objeto específico (por isso detail=False)
    def filtered(self, request):
        # ação personalizada para lidar com a lógica de filtragem e retorno dos resultados filtrados
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AvaliacaoViewSet(viewsets.ModelViewSet):
    """
        Função para cadastro das avaliações
    """
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
    authentication_classes= [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsInstrutor]

    def list(self, request, *args, **kwargs):
        queryset = Avaliacao.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = self.serializer_class(data=data)  # Remova many=True
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    # anotação usada para especificar na documentação que os campos de id sejam exibidos
    @swagger_auto_schema(manual_parameters=[
        openapi.Parameter('id_aprendiz', openapi.IN_QUERY, description="ID do aprendiz", type=openapi.TYPE_INTEGER),
        openapi.Parameter('id_semestre', openapi.IN_QUERY, description="ID do semestre", type=openapi.TYPE_INTEGER),
    ])

    @action(detail=False, methods=['get']) 
    def get_avaliacoes(self, request):
        """
            Nessa função é especificado o aprendiz e semestre e então, 
            são listados todos os critérios cadastrados na avaliação daquele semestre em formato JSON
        """
        # verificar se precisa alterar/retirar ou acrescentar algo nessa função
        id_aprendiz = request.query_params.get('id_aprendiz')
        id_semestre = request.query_params.get('id_semestre')

        avaliacoes = Avaliacao.objects.filter(idAprendiz=id_aprendiz, idSemestre=id_semestre)

        # avaliacoes = Avaliacao.objects.all()
        
        avaliacoes_json = []
        for avaliacao in avaliacoes:
            avaliacao_json = {
                "nota": str(avaliacao.nota),
                "idTurma": avaliacao.idTurma.id,  # .id - permite que o objeto seja serializável em JSON
                "idAprendiz": avaliacao.idAprendiz.id,
                "idSemestre": avaliacao.idSemestre.id,
                "idCriterio": avaliacao.idCriterio.id
            }
            avaliacoes_json.append(avaliacao_json)
        
        return Response(data=avaliacoes_json, status=status.HTTP_200_OK)


class AvaliacaoFiltroViewSet(viewsets.ModelViewSet):
    """
        Função para rota das notas que os instrutores adicionaram na avaliação 
        (filtro por turma, aprendiz, semestre e critério)
    """
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
    authentication_classes= [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsInstrutor]
    filter_backends = [DjangoFilterBackend] 
    filterset_class = AvaliacaoFilter 

    @action(detail=False, methods=['get']) 
    def filtered(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AutoAvaliacaoViewSet(viewsets.ModelViewSet):
    """
        Função para cadastro das autoavaliações
    """
    queryset = AutoAvaliacao.objects.all()
    serializer_class= AutoAvaliacaoSerializer
    authentication_classes= [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAprendiz]

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)   


class AutoAvFiltroViewSet(viewsets.ModelViewSet):
    """
        Função para rota das notas que os aprendizes adicionaram na autoavaliação 
        (filtro por semestre, aprendiz e turma)
    """
    queryset = AutoAvaliacao.objects.all()
    serializer_class= AutoAvaliacaoSerializer
    authentication_classes= [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsInstrutor]
    filter_backends = [DjangoFilterBackend] 
    filterset_class = AutoAvaliacaoFilter 

    def list(self, request, *args, **kwargs):
        queryset = self.serializer_class(data=request.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object() 
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def filtered(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class NotaSemestreViewSet(viewsets.ModelViewSet):
    """
        Exibir as notas de diferentes semestres (filtro de critérios)
    """
    queryset = Avaliacao.objects.all()
    serializer_class= AvaliacaoSerializer
    authentication_classes= [TokenAuthentication]
    permission_classes=[IsAuthenticated, IsInstrutor]
    filter_backends = [DjangoFilterBackend] 
    filterset_class = SemestreFilter

    @action(detail=False, methods=['get'])
    def filtered(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
