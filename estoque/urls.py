from django.urls import path
from estoque.views import cadastrarProdutos, inserirProduto, vizualizarProdutos, editarProdutos, updateProdutos, listarProdutos

urlpatterns = [
    path('cadastrar-produtos', cadastrarProdutos, name='cadastrar-produtos'),
    path('inserir-produto', inserirProduto, name='inserir-produto'),
    path('visualizar-produtos/<int:id>', vizualizarProdutos, name='visualizar-produtos'),
    path('editar-produtos/<int:id>', editarProdutos, name='editar-produtos'),
    path('upadate-produtos/<int:id>', updateProdutos, name='update-produtos'),
    path('listar-produtos', listarProdutos, name='listar-produtos'),
]
