<h1 align="left">Projeto ToDo-List</h1>

###

<p align="left">Meu nome é Tharlis S. Seixas</p>

###

<h2 align="left">Sobre o projeto</h2>

###

<p align="left">Projeto realizado afim de treinar o desenvolvimento web. O projeto é uma aplicação web simples fazendo uso de padrão de projeto MTV (Model, Template, View).</p>
<p aling="left">O projeto ToDo-List é uma lista de tarefas, que possui as seguinte funcionalidades: criar, editar, excluir e concluir as tarefas.</p>

###

<h2 align="left">Tecnologias e Frameworks utilizas no projeto</h2>

* Python
* Django
* SQL
* Bootstrap
* Git
* GitHub

###

<h2 align="left">Instruções de execução</h2>

Clonar o repositorio

```
git clone https://github.com/TharlisSampaio/todo-list.git
```
Após clonar o projeto, deve criar um ambiente virtual

```
python -m venv .venv
```

Para ativar o ambiente virtual basta executar o comando, em sisemas Windows

```
.\.venv\Scripts\activate
```

Instalar as dependencias

```
pip install  -r requirements.txt
```

Agora configurar as variaveis de ambiente, na pasta raiz do projeto criar um arquivo .env e dentro deste arquivo escrever as seguintes linhas

```
SECRET_KEY=gerar_no_site
DEBUG=True
ALLOWED_HOSTS=*
```
gerar_no_site: https://djecrety.ir/
Após gerar o SECRET_KEY basta substituir

Agora executar o seguinte comando:

```
python manage.py migrate
```
Ele lê os arquivos de migração gerados pelo makemigrations e executa as instruções necessárias para trazer o esquema do banco de dados atual para o estado desejado. Isso inclui criar tabelas, adicionar ou remover colunas, e até mesmo modificar os tipos de dados das colunas existentes.

Agora executar o projeto, basta executar o comando: 
```
python manage.py runserver
```

###