from rolepermissions.roles import AbstractUserRole

class Administrador(AbstractUserRole):
    available_permissions = {
        'cadastrar_turma': True,
        'editar_turma': True,
        'cadastrar_criterio': True,
        'editar_criterio': True,
        'gerenciar_aprendizes': True
    }


class Gestor(AbstractUserRole):
    available_permissions = {'visualizar_rendimento_turmas': True}


class Instrutor(AbstractUserRole):
    available_permissions = {
        'avaliar_turmas': True,
        'visualizar_rendimento_turmas': True,
        'visualizar_rendimento_alunos': True,
        'criar_notas': True,
        'visualizar_notas': True,
        'realizar_avaliacao': True
    }


class Aprendiz(AbstractUserRole):
    available_permissions = {
        'realizar_autoavaliacao': True,
        'visualizar_rendimento_pessoal': True
    }


# Mapeamento entre as classes de permissões e as classes de funções
permission_role_mapping = {
    'Aprendiz': Aprendiz,
    'Instrutor': Instrutor,
    'Gestor': Gestor,
    'Administrador': Administrador
}