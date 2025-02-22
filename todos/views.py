from django.views.generic import ListView
from todos.models import Todos


"""
O módulo views no Django é responsável por receber solicitações dos clientes,
processá-las e retornar respostas. As visualizações podem ser funções ou classes
que definem a lógica do aplicativo, incluindo o processamento de dados,
a renderização de modelos e a criação de respostas para o cliente.
"""


class TodosListView(ListView):
    model = Todos
