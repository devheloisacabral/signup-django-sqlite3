Projeto Signup Django SQLite3
Visão Geral
Bem-vindo ao projeto Signup Django SQLite3! Este projeto é uma aplicação web simples em Django que permite aos usuários se cadastrarem e visualizarem dados de usuário armazenados em um banco de dados SQLite3. O projeto está organizado com um aplicativo Django chamado app_signup e um projeto chamado project_signup.

Estrutura do Projeto
lua
Copy code
signup-django-sqlite3/
|-- project_signup/
|   |-- project_signup/
|   |   |-- __init__.py
|   |   |-- settings.py
|   |   |-- urls.py
|   |   |-- asgi.py
|   |   |-- wsgi.py
|-- app_signup/
|   |-- migrations/
|   |   |-- __init__.py
|   |-- templates/
|   |   |-- home.html
|   |   |-- users.html
|   |-- __init__.py
|   |-- admin.py
|   |-- apps.py
|   |-- models.py
|   |-- tests.py
|   |-- views.py
|-- db.sqlite3
|-- manage.py
|-- README.md
Instalação
Clone o repositório:
bash
Copy code
git clone https://github.com/seu-usuario/signup-django-sqlite3.git
cd signup-django-sqlite3
Crie um ambiente virtual (opcional, mas recomendado):
bash
Copy code
python3 -m venv venv
source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
Instale as dependências:
bash
Copy code
pip install -r requirements.txt
Aplique as migrações do banco de dados:
bash
Copy code
python manage.py migrate
Uso
Executando o Servidor de Desenvolvimento
Para executar o servidor de desenvolvimento, use o seguinte comando:

bash
Copy code
python manage.py runserver
Visite http://127.0.0.1:8000/ em seu navegador para acessar a aplicação.

Página Inicial
A página inicial está acessível em http://127.0.0.1:8000/ e contém um formulário de cadastro.

Página de Dados do Usuário
A página de dados do usuário está acessível em http://127.0.0.1:8000/users/ e exibe dados de usuário do banco de dados.

Banco de Dados
Este projeto utiliza o SQLite3 como banco de dados padrão. O arquivo do banco de dados é chamado db.sqlite3 e está localizado na raiz do projeto.

Templates
home.html: A página principal com um formulário de cadastro.
users.html: Exibe dados do usuário (user_id, nome e idade) recuperados do banco de dados.
