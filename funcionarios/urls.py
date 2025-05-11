from django.urls import path
from funcionarios.views import cadastrarFuncionarios, inserirFuncionario, visualizarFuncionario, editarFuncionario

urlpatterns = [
    path('cadastrar-funcionarios', cadastrarFuncionarios, name='cadastrar-funcionarios'),
    path('inserir-funcionario', inserirFuncionario, name='inserir-funcionario'),
    path('visualizar-funcionario/<int:id>', visualizarFuncionario, name='visualizar-funcionario'),
    path('editar-funcionario/<int:id>', editarFuncionario, name='editar-funcionario'),
]
