# agenda/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm  
from django.db.models import Q
from .models import Ramal

# --- DEFINIÇÃO DO FORMULÁRIO 
class RamalForm(ModelForm):
    class Meta:
        model = Ramal
        fields = ['nome', 'setor', 'numero']
# ----------------------------------------------------------

# View INDEX
def index(request):
    # Pega o termo que o usuário digitou na busca (se houver)
    busca = request.GET.get('busca')
    
    if busca:
        # Filtra ramais onde o Nome OU o Setor contenham o texto digitado
        # 'icontains' significa que ignora maiúsculas/minúsculas
        ramais = Ramal.objects.filter(
            Q(nome__icontains=busca) | Q(setor__icontains=busca)
        )
    else:
        # Se não tiver busca, traz tudo
        ramais = Ramal.objects.all()
    
    contexto = {
        'titulo': 'Lista de Ramais da CODERN', 
        'ramais': ramais
    }
    return render(request, 'agenda/index.html', contexto)

# 1. FUNÇÃO ADICIONAR (CREATE)
def adicionar_ramal(request):
    if request.method == 'POST':
        form = RamalForm(request.POST) # Agora ele encontra a classe logo acima
        if form.is_valid():
            form.save()
            return redirect('agenda:index') 
    else:
        form = RamalForm()

    contexto = {'form': form, 'titulo': 'Adicionar Novo Ramal'}
    return render(request, 'agenda/form_ramal.html', contexto)

# 2. FUNÇÃO EDITAR (UPDATE)
def editar_ramal(request, ramal_id):
    ramal = get_object_or_404(Ramal, pk=ramal_id)
    if request.method == 'POST':
        form = RamalForm(request.POST, instance=ramal)
        if form.is_valid():
            form.save()
            return redirect('agenda:index')
    else:
        form = RamalForm(instance=ramal)
    
    contexto = {'form': form, 'titulo': 'Editar Ramal'}
    return render(request, 'agenda/form_ramal.html', contexto)

# 3. FUNÇÃO EXCLUIR (DELETE)
def excluir_ramal(request, ramal_id):
    ramal = get_object_or_404(Ramal, pk=ramal_id)
    if request.method == 'POST':
        ramal.delete()
        return redirect('agenda:index')
    
    return render(request, 'agenda/confirmar_exclusao.html', {'ramal': ramal})