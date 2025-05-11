from django.urls import path
from funcionarios.views import cadastrarFuncionarios, inserirFuncionario

urlpatterns = [
    path('cadastrar-funcionarios', cadastrarFuncionarios, name='cadastrar-funcionarios'),
    path('inserir-funcionario', inserirFuncionario, name='inserir-funcionario'),
]
