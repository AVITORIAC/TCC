from django.contrib import admin
from api.models import *
from meinung.roles import *

class CursoAdmin(admin.ModelAdmin):
    """
        define como os dados desse modelo serão exibidos 
        e manipulados na interface administrativa do Django.
    """
    list_display = ('descricao', ) # quais campos do modelo serão exibidos na lista de registros no admin
    list_display_links = ('descricao', ) # quais campos da lista de registros são clicáveis e levam para a página de detalhes do registro
    list_per_page = 10 # quantos registros serão exibidos por página na lista de registros


class TurmaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'idInstrutor', 'idCurso')
    list_display_links = ('nome', )
    list_per_page = 10


class UsuarioAdmin(admin.ModelAdmin):
    # Define os campos a serem exibidos na lista de usuários
    list_display = ('edv', 'email', 'nome', 'cargo', 'idTurma', 'status', 'logado', 'get_permissions_display')
    readonly_fields = ('get_permissions_display',)
    list_display_links = ('nome', )
    list_per_page = 10


    def get_permissions_display(self, obj):
        """
            Função para exibir as permissões de um usuário 
            em uma coluna da lista de usuários no Django Admin
        """
        permissions = obj.get_permissions()
        if permissions:
            permission_names = Permission.objects.filter(codename__in=permissions).values_list('name', flat=True)
            return ', '.join(sorted(permission_names))
        return "Nenhuma permissão"

    get_permissions_display.short_description = 'Permissões'


admin.site.register(Curso, CursoAdmin)
admin.site.register(Turma, TurmaAdmin)
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Tipo_avaliacao)
admin.site.register(Estado)
admin.site.register(Nota_senai)
admin.site.register(Semestre)
admin.site.register(Observacao)
admin.site.register(Criterio)
admin.site.register(Avaliacao)
admin.site.register(AutoAvaliacao)
