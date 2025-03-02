from django.urls import path
from usuario.views import cadastrarUsuario, inserirUsuario

urlpatterns = [
    path('novo-usuario', cadastrarUsuario, name='novo-usuario'),
    path('inserir-usuario', inserirUsuario, name='inserir-usuario'),
]
