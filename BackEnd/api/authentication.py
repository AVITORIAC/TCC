from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed
from .models import ExpirandoToken


class ExpiraTokenAuth(TokenAuthentication):
    """
        Define um backend de autenticação personalizado para expiração do token
    """
    model = ExpirandoToken

    def verificar_credenciais(self, key):
        try:
            # Tenta recuperar o token usando a chave fornecida
            token = self.model.objects.select_related('user').get(key=key)
        except self.model.DoesNotExist:
            raise AuthenticationFailed('Token inválido')

        # Verifica se o usuário associado ao token está ativo
        if not token.user.is_active:
            raise AuthenticationFailed('Usuário inativo...')

        # Verifica se o token expirou
        elif token.is_expired():
            raise AuthenticationFailed('Token expirado')

        else:
            raise AuthenticationFailed('deu b.o')

        return (token.user, token)