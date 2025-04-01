from django.urls import path
from estoque.views import cadastrarProdutos

urlpatterns = [
    path('cadastrar-produtos', cadastrarProdutos, name='cadastrar-produtos'),
]
