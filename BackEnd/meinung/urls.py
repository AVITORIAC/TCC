"""
URL configuration for meinung project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from api import viewsets as apiviewsets
from rest_framework import routers
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from api import urls as apiurls

# documentação do swagger
schema_view = get_schema_view(
    openapi.Info(
        title="Meinung",
        default_version='v1',
        description="API Documentation",
        terms_of_service="https://www.example.com/policies/terms/",
        contact=openapi.Contact(email="meinung2024@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

route = routers.DefaultRouter()

route.register(r'arquivo', apiviewsets.ArquivoViewSet, basename="arquivo") # trata o excel
route.register(r'curso', apiviewsets.CursoViewSet, basename="curso")
route.register(r'turma', apiviewsets.TurmaViewSet, basename="turma")
route.register(r'tipo/avaliacao', apiviewsets.TipoViewSet, basename="tipo")
route.register(r'notas/senai', apiviewsets.NotaSenaiViewSet, basename="senai") # notas do senai
route.register(r'semestre', apiviewsets.SemestreViewSet, basename="semestre")
route.register(r'observacao', apiviewsets.ObservacaoViewSet, basename="observacao")
route.register(r'estado', apiviewsets.EstadoViewSet, basename="estado")
route.register(r'criterio', apiviewsets.CriterioViewSet, basename="criterio") # a rota continua com o mesmo nome, uma é para as rotas principais e outra com o filtro
route.register(r'criterio', apiviewsets.CriterioFiltroViewSet, basename="criterio-filtros")
route.register(r'avaliacao', apiviewsets.AvaliacaoViewSet, basename="avaliacao")
route.register(r'avaliacao', apiviewsets.AvaliacaoFiltroViewSet, basename="avaliacao-filtros")
route.register(r'autoavaliacao', apiviewsets.AutoAvaliacaoViewSet, basename="autoavaliacao")
route.register(r'autoavaliacao/filtros', apiviewsets.AutoAvFiltroViewSet, basename="autoavaliacao-filtros") # url de filtros precisa estar nesse formatoc para funcionar corretamente
route.register(r'notas/semestre', apiviewsets.NotaSemestreViewSet, basename="notas-semestre") # notas dos aprendizes por semestre


urlpatterns = [
    path('admin/', admin.site.urls),
    # doc
    path('api/v1/docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/v1/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    # rotas
    path('api/v1/', include(route.urls)),
    path('api/v1/', include(apiurls)),

]
