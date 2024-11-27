# codigos testes que não podem ser apagados ainda 


# post avaliação em formato json

#    def salva_avaliacao(self, request):
      #   if request.method == 'POST':
      #       data = json.loads(request.body)
      #       try:
      #           turma = Turma.objects.get(pk=data.get('idTurma'))
      #           aprendiz = Usuario.objects.get(pk=data.get('idAprendiz'))
      #           semestre = Semestre.objects.get(pk=data.get('idSemestre'))
      #           criterio = Criterio.objects.get(pk=data.get('idCriterio'))
      #           avaliacao = Avaliacao(
      #               idTurma=turma,  # Atribua a instância de Turma ao campo idTurma
      #               idAprendiz=aprendiz,
      #               idSemestre=semestre,
      #               idCriterio=criterio,
      #               nota=data.get('nota'),
      #           )
      #           avaliacao.save()
      #           return JsonResponse({'mensagem': 'Avaliação salva com sucesso!'})
      #       except Turma.DoesNotExist:
      #           return JsonResponse({'erro': 'Turma não encontrada'}, status=status.HTTP_404_NOT_FOUND)
      #       except Exception as e:
      #           return JsonResponse({'erro': str(e)}, status=status.HTTP_400_BAD_REQUEST)
      #   else:
      #       return JsonResponse({'erro': 'Método inválido'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)



# model usuario - permissões antigas



    # permissões referentes a cada grupo e seus diferentes acessos
    # permissions_aprendiz = [
    #     ('realizar_autoavaliacao', 'Realizar Autoavaliacao'),  
    #     ('visualizar_rendimento_pessoal', 'Visualizar Rendimento Pessoal')
    #     ]

    # permissions_instrutor = [
    #     ('avaliar_turmas', 'Avaliar Turmas'),  
    #     ('visualizar_rendimento_turmas', 'Visualizar Rendimento Turmas'), 
    #     ('visualizar_rendimento_alunos', 'Visualizar Rendimento Alunos'),
    #     ('criar_notas', 'Criar Notas'),
    #     ('visualizar_notas', 'Visualizar Notas'),
    #     ('realizar_avaliacao', 'Realizar Avaliação')
    #     ]

    # permissions_gestor = [('visualizar_rendimento_turmas', 'Visualizar Rendimento Turmas')]

    # permissions_admin = [
    #     ('cadastrar_turma', 'Cadastrar Turma'),
    #     ('editar_turma', 'Editar Turma'),
    #     ('cadastrar_criterio', 'Cadastrar Critério'),
    #     ('editar_criterio', 'Editar Critério'),
    #     ('gerenciar_aprendizes', 'Gerenciar Aprendizes')
    # ]





# if self.cargo:
#             group, created = Group.objects.get_or_create(name=self.cargo.capitalize())  # Capitaliza o nome do cargo para corresponder ao nome do grupo
#             permissions = []
#             if self.cargo == 'aprendiz':
#                 group, created = Group.objects.get_or_create(name='Aprendiz')
#                 permissions = Permission.objects.filter(codename__in=[perm[0] for perm in self.permissions_aprendiz]) # adiciona as roles exigidas em cada grupo
#                 group.permissions.set(permissions)
#                 self.groups.add(group)

#             elif self.cargo == 'instrutor':
#                 group, created = Group.objects.get_or_create(name='Instrutor')
#                 permissions = Permission.objects.filter(codename__in=[perm[0] for perm in self.permissions_instrutor])
#                 group.permissions.set(permissions)
#                 self.groups.add(group)

#             elif self.cargo == 'gestor':
#                 group, created = Group.objects.get_or_create(name='Gestor')
#                 permissions = Permission.objects.filter(codename__in=[perm[0] for perm in self.permissions_gestor])
#                 group.permissions.set(permissions)
#                 self.groups.add(group)

#             elif self.cargo == 'administrador':
#                 group, created = Group.objects.get_or_create(name='Administrador')
#                 permissions = Permission.objects.filter(codename__in=[perm[0] for perm in self.permissions_admin])
#                 group.permissions.set(permissions)
#                 self.groups.add(group)

#             else:
#                 return Response(data={"Verifique se esse cargo existe"}, status=status.HTTP_401_UNAUTHORIZED)
#         else:
#             return Response(data={"Erro...Tente Novamente"}, status=status.HTTP_400_BAD_REQUEST)





# admin - usuario - permissões antigas



# class UsuarioAdmin(admin.ModelAdmin):
#     # Define os campos a serem exibidos na lista de usuários
#     list_display = ('edv', 'email', 'nome', 'cargo', 'idTurma', 'status', 'logado', 'get_permissions_display')
#     list_display_links = ('nome', )
#     list_per_page = 10

#     # Define uma função para obter e exibir as permissões associadas a cada usuário
#     def get_permissions_display(self, obj):
#         # Verifica o cargo do usuário e retorna as permissões correspondentes
#         if obj.cargo == 'aprendiz':
#             return ', '.join([perm[1] for perm in obj.permissions_aprendiz])
#         elif obj.cargo == 'instrutor':
#             return ', '.join([perm[1] for perm in obj.permissions_instrutor])
#         elif obj.cargo == 'gestor':
#             return ', '.join([perm[1] for perm in obj.permissions_gestor])
#         elif obj.cargo == 'administrador':
#             return ', '.join([perm[1] for perm in obj.permissions_admin])
#         else:
#             return "cargo não reconhecido"  

#     # Define o nome exibido para a função get_permissions_display no admin do Django
#     get_permissions_display.short_description = 'Permissões'





# logout:


# class LogoutView(generics.GenericAPIView):
#     """
#         View para realizar o logout de um usuário autenticado.
#     """
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [IsAuthenticated]

#     def post(self, request):
#         # Recupera o token do cabeçalho de autorização
#         try:
#             token = Token.objects.get(user=request.user)
#         except Token.DoesNotExist:
#          return Response({"detail": "O token do usuário não foi encontrado."}, status=status.HTTP_404_NOT_FOUND)

#         try:
#             token.delete() # exclui o token
#             return Response({'message': 'Logout realizado com sucesso.'}, status=status.HTTP_200_OK)
#         except Exception as e:
#             return Response({'error': 'Ocorreu um erro ao realizar o logout.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
