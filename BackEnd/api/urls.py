from django.urls import path
from api.views import *

"""
    urls criadas para cadastros, login e
    redefinição das senhas
"""

urlpatterns = [
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('usuario/cadastro/', UsuarioView.as_view(), name="usuario"), # cadastro
    path('usuario/', UsuarioUpdateView.as_view(), name="usuario-lista"), # lista de todos os usuarios
    path('usuario/<int:pk>/', UsuarioUpdateView.as_view(), name="usuario-editar"), # editar cadastro de usuário
    path('admin/lista/', AdminListView.as_view(), name="admin-lista"),
    path('instrutor/lista/', InstrutorListView.as_view(), name="instrutor-lista"), # lista com todos os instrutores cadastrados
    path('instrutor/espera/', InstrutorEsperaListView.as_view(), name="instrutor-espera"), # lista com todos os instrutores que estão em espera
    path('instrutor/aprovado/', InstrutorAprovadoListView.as_view(), name="instrutor-aprovado"), # lista com todos os instrutores que estão aprovados
    path('gestor/lista/', GestorListView.as_view(), name="gestor-lista"), 
    path('gestor/espera/', GestorEsperaListView.as_view(), name="gestor-espera"), 
    path('gestor/aprovado/', GestorAprovadoListView.as_view(), name="gestor-aprovado"), 
    path('aprendiz/lista/', AllAprendizListView.as_view(), name="aprendiz-lista"), 
    path('aprendiz/espera/', AprendizEsperaListView.as_view(), name="aprendiz-espera"),
    path('aprendiz/aprovado/', AprendizAprovadoListView.as_view(), name="aprendiz-aprovado"),
    path('avaliacao/media/<int:idAprendiz>/<int:idTurma>/<int:idSemestre>/', MediaView.as_view(), name="media-notas"), # média das avaliações dos aprendizes
    path('avaliacao/detalhes/<int:idAprendiz>/<int:idSemestre>/', DetalhesAvaliacaoView.as_view(), name="detalhes-avaliacao"), # detalhes da avaliação por filtro
    path('rendimento/aprendiz/<int:id_semestre1>/<int:id_semestre2>/', RendimentoAprendizView.as_view(), name="aprendiz-rendimento"), # compara as notas entre 2 semestres
    path('rendimento/turmas/<int:turma1_id>/<int:turma2_id>/<int:semestre_id>/', CompararTurmasView.as_view(), name="comparar-turmas"), # compara as notas das turmas
    path('rendimento/aprendizes/<int:id_aprendiz1>/<int:id_aprendiz2>/<int:id_semestre>/<int:id_criterio>/', CompararAprendizesView.as_view(), name="comparar-aprendizes"), # compara as notas dos aprendizes
    path('feedback/<int:idAprendiz>/<int:idTurma>/<int:idSemestre>/', FeedbackView.as_view(), name="feedback"), # rota para o feedback do instrutor
    # recuperação de senha
    path('codigo/', CodigoView.as_view(), name="codigo"),
    path('ets/', EtsView.as_view(), name="ets"),
    path('recuperar/', RecuperarView.as_view(), name="recuperar"),
    # http://127.0.0.1:8000/api/v1/autoavaliacao/?idAprendiz=5&idSemestre=1 ---teste---
]
