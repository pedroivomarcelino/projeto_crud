from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from funcionarios.forms import FuncionarioForm
from funcionarios.models import Funcionario


#carrega a index de funcionarios
def listar_funcionarios(request):
    if request.session.get('usuario_logado'):
        funcionarios = Funcionario.objects.all()
        return render(request, 'funcionarios/index_funcionarios.html', {'funcionarios': funcionarios})
    else:
        return redirect('login')
    

#carrega a index de funcionarios inativos  
# views.py
def listar_funcionarios_inativos(request):
    if request.session.get('usuario_logado'):
        funcionarios = Funcionario.objects.filter(status_funcionario='inativo')
        return render(request, 'funcionarios/index_funcionario_inativo.html', {'funcionarios': funcionarios})
    else:
        return redirect('login')


#carrega o form de cadastro de funcionarios
def cadastrarFuncionarios(request):
    if request.session.get('usuario_logado'):
        
        return render(request, 'funcionarios/cadastrar_funcionarios.html')
        
    else:
        return redirect('login')
    
#carregar form de visualizar funcionarios
def visualizarFuncionario(request, id):
    if request.session.get('usuario_logado'):
        funcionarios = Funcionario.objects.get(id=id)
        return render(request, 'funcionarios/visualizar_funcionarios.html', {'funcionarios': funcionarios})
    else:
        return redirect('login')


#carregar form de edicao de funcionarios
def editarFuncionario(request, id):
    if request.session.get('usuario_logado'):
        funcionarios = Funcionario.objects.get(id=id)
        return render(request, 'funcionarios/editar_funcionarios.html', {'funcionarios': funcionarios})
    else:
        return redirect('login')

#metodo para inserir novos funcionarios no banco de dados
def inserirFuncionario(request):
    if request.session.get('usuario_logado'):
        
        if request.method == 'POST':
            
            form = FuncionarioForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Funcionário cadastrado com sucesso!")
                
            
            else:

                for field, errors in form.errors.items():
                    for error in errors:
                        messages.error(request, f"{form.fields[field].label}: {error}", extra_tags='danger')
        return redirect ('cadastrar-funcionarios')   
    else:
        return redirect('login')
    
#metodo para realizar a atualizacao de dados do funcionario
def update_funcionarios(request, id):
    if request.session.get('usuario_logado'):
        funcionarios = get_object_or_404(Funcionario, id=id)
        form = FuncionarioForm(request.POST or None, instance=funcionarios)
        if form.is_valid():
            form.save()
            messages.success(request, "Funcionário atualizado com sucesso!")
            return redirect('visualizar-funcionario', id=id)
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{form.fields[field].label}:{error}", extra_tags='danger')
        return redirect('editar-funcionario', id=id)
    else:
        return redirect('login')
                                   
        
        
#metodo para deletar funcionarios
def delete_funcionarios(request, id):
    if request.session.get('usuario_logado'):
        funcionarios = get_object_or_404(Funcionario, id=id)
        funcionarios.delete()
        messages.success(request, "Funcionário excluído com sucesso!")
        return redirect('listar-funcionarios')
    else:
        return redirect('login')
    
