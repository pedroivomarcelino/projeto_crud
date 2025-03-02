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

    def clean_nome_usuario(self):
        nome_usuario = self.cleaned_data.get('nome_usuario')
        valida_username_existe(nome_usuario)
        return nome_usuario
    
    def clean_login(self):
        login = self.cleaned_data.get('login')
        valida_login_existe(login)
        return login

    def clean_senha(self):
        senha = self.cleaned_data.get('senha')
        valida_tamanho_senha(senha)
        return senha
