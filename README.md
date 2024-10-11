# CRUD-API

## Apps
* users -> Abriga a inclusão de usuário, bem como as funções de listar, alterar e deletar.
* movies -> Abriga a inclusão de filmes, bem como as funções de listar, alterar e deletar.
* books -> Abriga a inclusão de livros, bem como as funções de listar, alterar e deletar.

## Organização
* Foi utilizado o Django Rest Framework - Indicado para a utilização de API's.
* Foi utilizado o método Serializer junto ao Generics do REST.
* Foi utilizado o banco de dados padrão do Django (db.sqlite3).

## Urls
* users
    * http://127.0.0.1:8000/api/users/
* movies
    * http://127.0.0.1:8000/api/movies/
* books
    * http://127.0.0.1:8000/api/books/

## Clonar repositório (Visual Studio Code)
* <b>Primeiro passo:</b> Crie uma pasta aonde quiser.
* <b>Segundo passo:</b> Abra-a no Visual Studio Code como um folder.
* <b>Terceiro passo:</b> Clone o repositório:
   ```bash
   git clone https://github.com/LUIZAUGUSTO1113/crud-api.git
   ```
* <b>Quarto passo:</b> Abra o terminal dentro do Vs code e digite:
   ``` bash
   dir
   ```
* <b>Quinto passo:</b> Agora digite:
   ``` bash
   cd crud-api
   ```
* <b>Sexto passo:</b> Crie uma venv pelo terminal:
   ``` bash
   python -m venv venv
   ```
* <b>Sétimo passo:</b> Ative a venv:
  ``` bash
  venv\Scripts\activate
  ```
* <b>Oitavo passo:</b> Instale os requisitos:
  ``` bash
  pip install -r requirements.txt
  ```
* <b>Nono passo:</b> Inicie o site:
  ``` bash
  python manage.py runserver
  ```
## @ 2024 1113
