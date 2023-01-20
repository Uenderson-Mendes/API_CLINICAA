from django.urls import path,include
from . import views 
from django.contrib import admin
from django.urls import path, include
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from agenda.views import ClientesViewSet, EspecialidadeViewSet, AgendaMViewSet,ConsultaViewSet, CadastrarViewSet #formu


router = routers.DefaultRouter()
router.register('especialidade',EspecialidadeViewSet)
router.register('cadastrar', CadastrarViewSet)
router.register('agenda', AgendaMViewSet)
router.register('clientes', ClientesViewSet)
router.register('consulta', ConsultaViewSet)

urlpatterns = [
    path('', include(router.urls) ),
   # path('cadastro/',views.formu, name='formu'),
     
    ]