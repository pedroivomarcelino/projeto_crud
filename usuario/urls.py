from django.urls import path
from usuario.views import cadastrarUsuario, inserirUsuario, indexUsuarios, visualizarUsuario

urlpatterns = [
    path('novo-usuario', cadastrarUsuario, name='novo-usuario'),
    path('inserir-usuario', inserirUsuario, name='inserir-usuario'),
    path('usuario-index', indexUsuarios, name='usuario-index'),
    path('visualizar-usuario/<int:id>', visualizarUsuario, name='visualizar-usuario' )
]
