from django.urls import path
from funcionarios.views import cadastrarFuncionarios

urlpatterns = [
    path('cadastrar-funcionarios', cadastrarFuncionarios, name='cadastrar-funcionarios'),
]
