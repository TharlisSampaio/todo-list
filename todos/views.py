from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
from todos.models import Todos
from django.shortcuts import redirect
from datetime import datetime


"""
O módulo views no Django é responsável por receber solicitações dos clientes,
processá-las e retornar respostas. As visualizações podem ser funções ou classes
que definem a lógica do aplicativo, incluindo o processamento de dados,
a renderização de modelos e a criação de respostas para o cliente.
"""


class TodosListView(ListView):
    model = Todos


class TodoCreateView(CreateView):
    model = Todos
    fields = ["title", "deadline"]
    success_url = reverse_lazy("todo_list")


class TodoUpdateView(UpdateView):
    model = Todos
    fields = ["title", "deadline"]
    success_url = reverse_lazy("todo_list")


class TodoDeleteView(DeleteView):
    model = Todos
    success_url = reverse_lazy("todo_list")


class TodoCompleteView(View):
    def get(self, request, pk):
        todo = Todos.objects.get(pk=pk)
        todo.finished_at = datetime.now()
        todo.save()
        return redirect("todo_list")
