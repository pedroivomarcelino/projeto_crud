from django.urls import path
from estoque.views import cadastrarProdutos, inserirProduto, vizualizarProdutos

urlpatterns = [
    path('cadastrar-produtos', cadastrarProdutos, name='cadastrar-produtos'),
    path('inserir-produto', inserirProduto, name='inserir-produto'),
    path('visualizar-produtos/<int:id>', vizualizarProdutos, name='visualizar-produtos'),
]
