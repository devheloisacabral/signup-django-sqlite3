# Signup Django SQLite3

## Visão Geral

Olá! Esse é o Signup Django SQLite3, um projeto de aplicação web simples para cadastro de usuários pelo nome e idade que serão visualizados junto com todos os usuarios do banco. Aqui eu utilizo Django e SQLite3. 🚀

## Estrutura do Projeto

```
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
```

## Instalação

1. Clone o repositório:

```bash
git clone https://github.com/devheloisacabral/signup-django-sqlite3.git
cd signup-django-sqlite3
```

2. Aplique as migrações do banco de dados:

```bash
python manage.py migrate
```

## Uso

### Executando o Servidor de Desenvolvimento

Para iniciar o servidor de desenvolvimento, utilize o seguinte comando:

```bash
python manage.py runserver
```

Visite `http://127.0.0.1:8000/` em seu navegador para acessar a aplicação.

### Página Inicial

A página inicial, disponível em `http://127.0.0.1:8000/`, contém um formulário de cadastro contendo dois inputs dentro de um formulário que envia para uma rota named= 'list'📝

### Página de Dados do Usuário

A página de dados do usuário, acessível em `http://127.0.0.1:8000/users/`, exibe informações do usuário (user_id, nome e idade) recuperadas do banco de dados. 📊

## Banco de Dados

Este projeto utiliza o SQLite3 como banco de dados padrão. O arquivo do banco de dados é chamado `db.sqlite3`.

## Templates

- `home.html`: A página principal com um formulário de cadastro.
- `users.html`: Exibe dados do usuário (user_id, nome e idade) recuperados do banco de dados.

## Prints 

![Captura de tela de 2024-02-16 17-24-27](https://github.com/devheloisacabral/signup-django-sqlite3/assets/108575773/4a219a75-ef87-45c6-adcc-3b224757bb8d)


![image](https://github.com/devheloisacabral/signup-django-sqlite3/assets/108575773/b73c24d0-ce63-4562-8356-75f0916c6b4b)



Obrigada pela sua atenção! <3
