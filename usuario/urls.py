from django.urls import path
from usuario.views import cadastrarUsuario, inserirUsuario, indexUsuarios, visualizarUsuario, editarUsuario, updateUsuario

urlpatterns = [
    path('novo-usuario', cadastrarUsuario, name='novo-usuario'),
    path('inserir-usuario', inserirUsuario, name='inserir-usuario'),
    path('usuario-index', indexUsuarios, name='usuario-index'),
    path('visualizar-usuario/<int:id>', visualizarUsuario, name='visualizar-usuario'),
    path('editar-usuario/<int:id>', editarUsuario, name='editar-usuario'),
    path('update-usuario/<int:id>', updateUsuario, name='update-usuario'),
]
