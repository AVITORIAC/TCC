import django_filters
from .models import *

# arquivo que contém as classes necessárias para os filtros


class AutoAvaliacaoFilter(django_filters.FilterSet):
    # notas que os aprendizes adicionaram na autoavaliação

    idTurma = django_filters.NumberFilter(field_name='idTurma')
    idAprendiz = django_filters.NumberFilter(field_name='idAprendiz')
    idSemestre = django_filters.NumberFilter(field_name='idSemestre')

    class Meta:
        model = AutoAvaliacao
        fields = ['idTurma', 'idAprendiz', 'idSemestre']


class AvaliacaoFilter(django_filters.FilterSet):
    # notas que os instrutores adicionaram na avaliação

    idTurma = django_filters.NumberFilter(field_name='idTurma')
    idAprendiz = django_filters.NumberFilter(field_name='idAprendiz')
    idSemestre = django_filters.NumberFilter(field_name='idSemestre')
    idCriterio = django_filters.NumberFilter(field_name='idCriterio')

    class Meta:
        model = Avaliacao
        fields = ['idTurma', 'idAprendiz', 'idSemestre', 'idCriterio']


class SemestreFilter(django_filters.FilterSet):
    # Exibir as notas de diferentes semestres (filtro de critérios)

    idCriterio = django_filters.NumberFilter(field_name='idCriterio') 

    class Meta:
        model = Avaliacao
        fields = ['idCriterio']


class CriterioFilter(django_filters.FilterSet):
    # rota de rendimento selecionando o tipo e critério (instrutor)

    idTipo_avaliacao = django_filters.NumberFilter(field_name='idTipo_avaliacao')
    id = django_filters.NumberFilter(field_name='id') # id do critério a ser filtrado

    class Meta:
        model = Criterio
        fields = ['idTipo_avaliacao', 'id']

