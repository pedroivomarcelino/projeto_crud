from django.shortcuts import render, redirect, get_object_or_404
from usuario.forms import UsuarioForm
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.models import User
from usuario.models import Usuario

#abre o form de cadastro de usuario
def cadastrarUsuario(request):
    if request.session.get('usuario_logado'):
        return render(request, 'usuarios/cadastrar_usuarios.html')
    else:
        return redirect('login')

#exibe todos os usuarios cadastrados
def indexUsuarios(request):
    if request.session.get('usuario_logado'):
        usuario_id = request.session['usuario_logado']
        usuario = Usuario.objects.get(id=usuario_id)
        usuarios = Usuario.objects.all()
        return render(request, 'usuarios/index_usuarios.html', {'usuarios': usuarios, 'usuario': usuario})
    else:
        return redirect('login')
    
#metodo para cadastrar um novo usuario no banco de dados
def inserirUsuario(request):
    if request.session.get('usuario_logado'):
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
    else:
        return redirect('login')
    
    
#abre a tela com o form preenchido com os dados do usuario            
def visualizarUsuario(request, id):
    if request.session.get('usuario_logado'):
        usuarios = Usuario.objects.filter(id=id)
        return render(request, 'usuarios/visualizar_usuarios.html', {'usuarios' : usuarios})
    else:
        return redirect('login')


#abre a tela com os dados do usuario para edição
def editarUsuario(request, id):
    if request.session.get('usuario_logado'):
        usuarios = Usuario.objects.filter(id=id)
        return render(request, 'usuarios/editar_usuarios.html', {'usuarios' : usuarios})
    else:
        return redirect('login')

#metodo responsavel por atualizar os dados do usuario no banco de dados
def updateUsuario(request, id):
    if request.session.get('usuario_logado'):
        usuarios = get_object_or_404(Usuario, id=id)
        if request.method == 'POST':
            form = UsuarioForm(request.POST, instance=usuarios)
            if form.is_valid():
                form.save()
                messages.success(request, 'Usuário atualizado com sucesso!')
                return redirect('visualizar-usuario', id=id)
            else:
                messages.error(request, 'Erro ao atualizar o usuário. Verifique os dados e tente novamente.')
                for field, errors in form.errors.items():
                    for error in errors:
                        messages.error(request, f"{form.fields[field].label}: {error}", extra_tags='danger')
            return redirect('editar-usuario', id=id)
        else:
            form = UsuarioForm(instance=usuarios)

        return redirect('usuario-index')
    else:
        return redirect('login')

#metodo responsavel por excluir o usuario do banco de dados
def excluirUsuario(request, id):
    if request.session.get('usuario_logado'):
        usuarios = Usuario.objects.filter(id=id)
        usuarios.delete()
        messages.success(request, 'Usuário excluído com sucesso!')
        return redirect('usuario-index')
    else:
        return redirect('login')
            
            
    
def usuario_logado(request):
    usuario = None
    if request.session.get('usuario_logado'):  # Verifica se há um usuário na sessão
        usuario_id = request.session['usuario_logado']
        request.session.modified = True
        usuario = Usuario.objects.filter(id=usuario_id).first()
        
    return {'usuario': usuario} 
