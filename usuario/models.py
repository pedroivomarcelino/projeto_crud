from django.db import models
from django.contrib.auth.hashers import make_password

class Usuario(models.Model):
    nome_usuario = models.CharField(max_length=255, null=False, blank=False)
    login = models.CharField(max_length=255, null=False, blank=False)
    senha = models.CharField(max_length=255, null=False, blank=False)
    
    def set_senha(self, senha):
        """Define a senha usando hash seguro"""
        self.senha = make_password(senha)  # Aplica o hash

    def save(self, *args, **kwargs):
        """Sobrescreve o método save para garantir que a senha seja armazenada com hash"""
        if not self.senha.startswith('pbkdf2_'):  # Evita re-hashear senhas já criptografadas
            self.senha = make_password(self.senha)
        super().save(*args, **kwargs)   
        
    def __str__(self):
        return self.nome_usuario
