from rest_framework import permissions

# arquivo para checar as permissões e acessos de cada tipo de usuário

class IsInstrutor(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        """
            verifica  se o usuário tem permissão para realizar uma ação em um objeto específico 
            (como recuperar, atualizar ou excluir um objeto específico)
        """

        return super().has_object_permission(request, view, obj)

        # Verifica se o método da requisição é seguro
        # if request.method in permissions.SAFE_METHODS:
        #     return True
        
        # Verifica se o usuário é o autor do objeto
        # elif obj.owner == request.user:
        #     return True
        
        # Se nenhuma condição acima for atendida, nega a permissão
        # else:
        #     return False

    def has_permission(self, request, view): 
        """
            verifica se o usuário tem permissão para acessar a view em geral
        """
        if not request.user.is_authenticated:
            return False
        return request.user.check_user_role('Instrutor')
        # return request.user.groups.filter(name='Instrutor').exists()

class IsAprendiz(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return super().has_object_permission(request, view, obj)

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        return request.user.check_user_role('Aprendiz')

class IsGestor(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return super().has_object_permission(request, view, obj)

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        return request.user.check_user_role('Gestor')


class IsAdministrador(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return super().has_object_permission(request, view, obj)

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        return request.user.check_user_role('Administrador')

        