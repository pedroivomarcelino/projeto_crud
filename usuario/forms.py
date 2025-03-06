from django import forms
from usuario.models import Usuario
from usuario.validator import valida_username_existe, valida_tamanho_senha, valida_login_existe

class UsuarioForm(forms.ModelForm):
    class Meta:  
        model = Usuario
        fields = [
            'nome_usuario',
            'login',
            'senha',
        ]
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.instance_original = kwargs.get('instance')

    def clean_nome_usuario(self):
        nome_usuario = self.cleaned_data.get('nome_usuario')
        
        # Se o nome não foi alterado, retorna sem validar
        if self.instance_original and self.instance_original.nome_usuario == nome_usuario:
            return nome_usuario
        
        # Se o nome foi alterado, valida o nome
        valida_username_existe(nome_usuario)
        return nome_usuario
    
    def clean_login(self):
        login = self.cleaned_data.get('login')
        
        # Se o login não foi alterado, retorna sem validar
        if self.instance_original and self.instance_original.login == login:
            return login
        
        # Se o login foi alterado, valida o login
        valida_login_existe(login)
        return login

    def clean_senha(self):
        senha = self.cleaned_data.get('senha')
        valida_tamanho_senha(senha)
        return senha
