# 📝 Projeto Ramal - Agenda Corporativa

Este é um sistema de gerenciamento de ramais desenvolvido com **Django** e **MySQL**. O projeto permite o cadastro, consulta, edição e exclusão de contatos internos (CRUD completo), contando também com uma barra de busca dinâmica integrada ao banco de dados.



## 🚀 Funcionalidades

* **Listagem Dinâmica:** Visualização de todos os ramais cadastrados em uma tabela organizada.
* **Busca Inteligente:** Filtro por nome ou setor processado via servidor (Python/Django).
* **Gerenciamento Completo (CRUD):**
    * **Create:** Adicionar novo ramal através de formulários validados.
    * **Read:** Visualização clara dos dados com suporte a busca.
    * **Update:** Edição de informações de contatos já existentes.
    * **Delete:** Exclusão de registros com interface amigável.
* **Interface Responsiva:** Desenvolvida com **Bootstrap 5**, garantindo bom visual em qualquer tamanho de tela.
* **Segurança:** Proteção contra ataques CSRF nativa do Django.

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3.13
* **Framework Web:** Django
* **Banco de Dados:** MySQL
* **Frontend:** HTML5, Bootstrap 5, Bootstrap Icons
* **Estilização:** CSS3 Customizado

## 📂 Estrutura do Projeto

* `setup/`: Configurações principais do projeto (settings, urls).
* `agenda/`: Aplicativo principal.
    * `models.py`: Definição da tabela `Ramal` e seus campos.
    * `views.py`: Lógica de negócio (Processamento da busca e funções CRUD).
    * `templates/`: Interface do usuário (HTML com Django Template Language).
* `static/`: Armazenamento de arquivos CSS e JS para personalização visual.



## 🔧 Como instalar e rodar o projeto

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/seu-usuario/projeto-ramal.git](https://github.com/seu-usuario/projeto-ramal.git)
   cd projeto-ramal
Instale o driver do MySQL (mysqlclient):

Bash
pip install mysqlclient
Configure o Banco de Dados: No arquivo setup/settings.py, localize o bloco DATABASES e insira suas credenciais locais:

Python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'nome_do_seu_banco',
        'USER': 'seu_usuario',
        'PASSWORD': 'sua_senha',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
Aplique as Migrações:

Bash
python manage.py migrate
Inicie o servidor:

Bash
python manage.py runserver
O projeto estará disponível em: http://127.0.0.1:8000

Desenvolvido por Seu Nome como parte de estudos em Python & Django.
