# agenda/admin.py
from django.contrib import admin
from .models import Ramal  # Importa a classe Ramal que você criou

# 1. (Opcional) Crie uma classe de personalização para o Admin
admin.site.register(Ramal)
class RamalAdmin(admin.ModelAdmin):
    # Campos que serão mostrados na lista principal do Admin
    list_display = ('nome', 'numero', 'setor', 'email')
    
    # Adiciona uma caixa de pesquisa que busca nesses campos
    search_fields = ('nome', 'numero', 'setor')
    
    # Adiciona um filtro lateral por setor
    list_filter = ('setor',)

    # Torna o campo 'numero' um link para a página de edição
    list_display_links = ('numero',)