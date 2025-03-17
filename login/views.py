from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth.hashers import check_password
from usuario.models import Usuario
from django.contrib import messages

def login(request):
    return render(request, 'login/login.html')


def logar(request):
    if request.method == 'POST':
        # Obter os valores dos campos do formulário
        login = request.POST.get('login')
        senha = request.POST.get('senha')  
        
        try:
            # Verificar se o usuário existe no banco de dados
            usuario = Usuario.objects.get(login=login)
            
            #verificar se a senha está correta
            if check_password(senha, usuario.senha):
                
                #se o login e senha estiverem corretos, redirecionar para a página inicial
                request.session['usuario_logado'] = usuario.id
                #print(f"Usuário {usuario.id} logado com sucesso!")
                return redirect('index')
        
            #em caso de erro, exibir mensagem de erro
            else:
                messages.error(request, 'Usuário ou senha inválidos')
                return render(request, 'login/login.html')
            
        #verificar se o usuário nao existe
        except Usuario.DoesNotExist:
            
                messages.error(request, 'Usuário não encontrado')
                return render(request, 'login/login.html')
    
    return render(request, 'login/login.html')
    
def logout(request):
    request.session.clear()
    return redirect('login')