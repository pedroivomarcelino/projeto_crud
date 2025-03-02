from django.shortcuts import render, redirect
from usuario.forms import UsuarioForm
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.models import User
from usuario.models import Usuario

def cadastrarUsuario(request):
    return render(request, 'usuarios/cadastrar_usuarios.html')

def indexUsuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuarios/index_usuarios.html', {'usuarios': usuarios})

def inserirUsuario(request):
    form = UsuarioForm()
    
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuário cadastrado com sucesso!')
            return redirect('novo-usuario')
        else:
            messages.error(request, 'Erro ao cadastrar o usuário. Verifique os dados e tente novamente.')
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{form.fields[field].label}: {error}", extra_tags='danger')
                    
    return redirect('novo-usuario')
            
def visualizarUsuario(request, id):
    usuarios = Usuario.objects.filter(id=id)
    return render(request, 'usuarios/visualizar_usuarios.html', {'usuarios' : usuarios})


            
            
    
    
