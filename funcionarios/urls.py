from django.urls import path
from funcionarios.views import cadastrarFuncionarios, inserirFuncionario, visualizarFuncionario, editarFuncionario, update_funcionarios, listar_funcionarios, delete_funcionarios, listar_funcionarios_inativos

urlpatterns = [
    
    path('cadastrar-funcionarios', cadastrarFuncionarios, name='cadastrar-funcionarios'),
    path('inserir-funcionario', inserirFuncionario, name='inserir-funcionario'),
    path('visualizar-funcionario/<int:id>', visualizarFuncionario, name='visualizar-funcionario'),
    path('editar-funcionario/<int:id>', editarFuncionario, name='editar-funcionario'),
    path('update_funcionarios/<int:id>', update_funcionarios, name='update_funcionarios'),
    path('listar-funcionarios', listar_funcionarios, name='listar-funcionarios'),
    path('delete_funcionarios/<int:id>', delete_funcionarios, name='delete-funcionarios'),
    path('listar-funcionarios-inativos', listar_funcionarios_inativos, name='listar-funcionarios-inativos'),
]
