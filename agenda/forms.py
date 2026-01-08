# agenda/forms.py
from django.forms import ModelForm
from .models import Ramal

# O ModelForm é a maneira mais fácil de criar formulários
# que correspondem a um modelo de banco de dados.
class RamalForm(ModelForm):
    class Meta:
        model = Ramal
        # Campos que aparecerão no formulário:
        fields = ['nome', 'setor', 'numero']