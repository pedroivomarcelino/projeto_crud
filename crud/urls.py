from django.urls import path
from crud.views import index, cadastrarCliente, inserirCliente, exibirClientes,visualizarCliente, formEditarCliente, updateClientes, excluirCliente

urlpatterns = [
    path('', index, name='index'),
    path('cadastrar-cliente', cadastrarCliente, name='cadastrar-cliente'),
    path('inserir-cliente', inserirCliente, name='inserir-cliente'),
    path('cliente-index', exibirClientes, name='cliente-index'),
    path('visualizar-cliente/<int:id>', visualizarCliente, name='visualizar-cliente'),
    path('editar-cliente/<int:id>', formEditarCliente, name='editar-cliente'),
    path('update-cliente/<int:id>', updateClientes, name='update-cliente'),
    path('deletar-cliente/<int:id>', excluirCliente, name='deletar-cliente'),
]
