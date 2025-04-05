from django.urls import path
from estoque.views import cadastrarProdutos, inserirProduto

urlpatterns = [
    path('cadastrar-produtos', cadastrarProdutos, name='cadastrar-produtos'),
    path('inserir-produto', inserirProduto, name='inserir-produto'),
]
