from django.core.exceptions import ValidationError
from usuario.models import Usuario

def valida_username_existe(nome_usuario):
    """Verifica se o username já existe cadastrado no banco de dados."""
    if Usuario.objects.filter(nome_usuario=nome_usuario).exists():
        raise ValidationError("Username já cadastrado no sistema")
    
def valida_login_existe(login):
    """Verificar se o e-mail do login ja existe"""
    if Usuario.objects.filter(login=login).exists():
        raise ValidationError("O e-mail ja cadastrado no sistema ")
    
def valida_tamanho_senha(senha):
    """Verifica se a senha tem no mínimo 8 caracteres."""
    if len(senha) < 8:
        raise ValidationError("A senha deve conter no mínimo 8 caracteres")


