from django.db import models


class Todos(models.Model):
    # max_length: maximo de caracteres; null=False: no banco de dados não aceitra campo null
    # blank=False: no banco não aceita campo em branco
    title = models.CharField(max_length=100, null=False, blank=False)
    # auto_now_add=True: insere a data que foi criado a tarefa
    created_at = models.DateField(auto_now_add=True, null=False, blank=False)
    deadline = models.DateField(null=False, blank=False)
    finished_at = models.DateField(null=True)


"""
Migrate é responsável por aplicar e desaplicar migrações,
enquanto makemigrations cria novas migrações com base nas alterações
feitas nos modelos1234. Migração é a forma do Django de propagar as
alterações feitas em seu modelo ao esquema do banco de dados4.
"""
