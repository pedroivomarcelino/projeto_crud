from django.shortcuts import render, redirect, get_object_or_404
from crud.forms import ClienteForm
from django.contrib import messages
from crud.models import Cliente


#view da página inicial
def index(request):
    if request.session.get('usuario_logado'):
        return render(request, 'index.html')
    else:
        return redirect('login')


#view de clientes

#carregar o form de cadastro de clientes
def cadastrarCliente(request):
    if request.session.get('usuario_logado'):
        return render(request, 'clientes/cadastrar_clientes.html')
    else:
        return redirect('login')

#funcao para inserir novos clientes no banco de dados
def inserirCliente(request):
    if request.session.get('usuario_logado'):
        if request.method == 'POST':
            form = ClienteForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Cliente cadastrado com sucesso!")
            else:
                messages.error(request, "Erro ao cadastrar o cliente. Verifique os dados e tente novamente.")
                
                for field, errors in form.errors.items():
                    for error in errors:
                        messages.error(request, f"{form.fields[field].label}: {error}", extra_tags='danger')            
                        
        return redirect ('cadastrar-cliente')
    else:
        return redirect('login')
    
#exibir todos os clientes cadastrados na tabela
def exibirClientes(request):
    if request.session.get('usuario_logado'):
        clientes = Cliente.objects.all() 
        return render(request, 'clientes/index_clientes.html', {'clientes': clientes})
    else:
        return redirect('login')

#carregar form de visualizacao de clientes
def visualizarCliente(request, id):
    if request.session.get('usuario_logado'):
        cliente = Cliente.objects.get(id=id)
        return render(request, 'clientes/visualizar_clientes.html', {'cliente': cliente})
    else:
        return redirect('login')

#carregar o form de edição de clientes
def formEditarCliente(request, id):
    if request.session.get('usuario_logado'):
        cliente = Cliente.objects.get(id=id)
        return render(request, 'clientes/editar_clientes.html', {'cliente': cliente})
    else:
        return redirect('login')

#metodo update para editar dados dos clientes
def updateClientes(request, id):
    if request.session.get('usuario_logado'):
        #recuperando dados do banco
        cliente = get_object_or_404(Cliente, id=id)
        
        if request.method == 'POST':
            #passando os dados do banco para o formulario
            form = ClienteForm(request.POST, instance=cliente)
            #validando se o form é valido
            if form.is_valid():
                #salvando os dados no banco
                form.save()
                messages.success(request, "Cliente atualizado com sucesso!")
            else:  
                messages.error(request, "Erro ao atualizar o cliente. Verifique os dados e tente novamente.")
                
                for field, errors in form.errors.items():
                    for error in errors:
                        messages.error(request, f"{form.fields[field].label}: {error}", extra_tags='danger')
                        return redirect('editar-cliente', id=id)
                        
        else:
            form = ClienteForm(instance=cliente)
            
        return redirect('cliente-index')    
    else:
        return redirect('login')

#metodo para exclusao de cliente
def excluirCliente(request, id):
    if request.session.get('usuario_logado'):
        cliente = Cliente.objects.get(id=id)
        cliente.delete()
        messages.success(request, "Cliente excluído com sucesso!")
        return redirect('cliente-index')
    else:
        return redirect('login')