from django.shortcuts import render, redirect, get_object_or_404
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

def editarUsuario(request, id):
    usuarios = Usuario.objects.filter(id=id)
    return render(request, 'usuarios/editar_usuarios.html', {'usuarios' : usuarios})

def updateUsuario(request, id):
    usuarios = get_object_or_404(Usuario, id=id)
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuarios)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuário atualizado com sucesso!')
            return redirect('usuario-index')
        else:
            messages.error(request, 'Erro ao atualizar o usuário. Verifique os dados e tente novamente.')
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{form.fields[field].label}: {error}", extra_tags='danger')
        return redirect('editar-usuario', id=id)
    else:
        form = UsuarioForm(instance=usuarios)

    return redirect('usuario-index')

def excluirUsuario(request, id):
    usuarios = Usuario.objects.filter(id=id)
    usuarios.delete()
    messages.success(request, 'Usuário excluído com sucesso!')
    return redirect('usuario-index')

            
            
    
    
