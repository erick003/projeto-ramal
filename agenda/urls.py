# agenda/urls.py 

from django.urls import path 
from . import views

# OU SE PREFERIR MANTER O INCLUDE NO IMPORT CASO USE EM OUTROS ARQUIVOS:
# from django.urls import path, include 

app_name = 'agenda'

urlpatterns = [
    # ROTAS DO APP AGENDA (Direcionam para as Views)
    path('', views.index, name='index'), 
    path('adicionar/', views.adicionar_ramal, name='adicionar_ramal'),
    path('editar/<int:ramal_id>/', views.editar_ramal, name='editar_ramal'),
    path('excluir/<int:ramal_id>/', views.excluir_ramal, name='excluir_ramal'), 
]