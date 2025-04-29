from django.shortcuts import render, redirect, get_object_or_404
from estoque.forms import ProdutoForm
from django.contrib import messages
from estoque.models import Produto


#carregar o form de cadastrar novos produtos no estoque
def cadastrarProdutos(request):
    
    if request.session.get('usuario_logado'):
        return render(request, 'estoque/cadastrar_produto.html')
    else:
        return redirect('login')

#carregar o form de vizualizacao dos produtos cadastrados no estoque
def vizualizarProdutos(request, id):

    if request.session.get('usuario_logado'):
        
        produtos = Produto.objects.get(id=id)
        return render(request, 'estoque/visualisar_produto.html', {'produtos': produtos})
    else:
        return redirect('login')

#carrega o form de edicao de produtos
def editarProdutos(request, id):
    
    if request.session.get('usuario_logado'):
        produtos = Produto.objects.get(id=id)
        return render(request, 'estoque/editar_produto.html', {'produtos': produtos})
    else:
        return redirect('login')
    

#funcao para recuperar todos os produtos cadastrados
def listarProdutos(request):
    if request.session.get('usuario_logado'):
        produtos = Produto.objects.all()
        return render(request, 'estoque/index_estoque.html', {'produtos': produtos})
    else:
        return redirect('login')

#funcao para inserir novos produtos no banco de dados
def inserirProduto(request):

    if request.session.get('usuario_logado'):
        if request.method == 'POST':
            
            form = ProdutoForm(request.POST)
            
            if form.is_valid():
                form.save()
                messages.success(request, "Produto cadastrado com sucesso!")
            
            else:
                messages.error(request, "Erro ao cadastrar o produto. Verifique os dados e tente novamente.")

                for field, errors in form.errors.items():
                    for error in errors:
                        messages.error(request, f"{form.fields[field].label}: {error}", extra_tags='danger')
                        
        return redirect('cadastrar-produtos')
    else:
        return redirect('login')

#funcao para atualizar os produtos cadastrados no banco de dados
def updateProdutos(request, id):
    
    if request.session.get('usuario_logado'):
        produtos = get_object_or_404(Produto, id=id)
        
        if request.method == 'POST':
        
            form = ProdutoForm(request.POST, instance=produtos)
            if form.is_valid():
                form.save()
                messages.success(request, "Produto atualizado com sucesso!")
            else:
                messages.error(request, "Erro ao atualizar o produto. Verifique os dados e tente novamente.")
                for field, errors in form.errors.items():
                    for error in errors:
                        messages.error(request, f"{form.fields[field].label}: {error}", extra_tags='danger')
                        return redirect('editar-produtos', id=id)
        
        else:
            form = ProdutoForm(instance=produtos)
            
        return redirect('visualizar-produtos', id=id) 
    else:
        return redirect('login')             
    
    
#excluir um produto do estoque
def deleteProduto(request, id):
    
    if request.session.get('usuario_logado'):
        
        produtos = get_object_or_404(Produto, id=id)
        if produtos.quantidade_produto > 0:
            messages.error(request, f"Produto não pode ser excluído, pois possui {produtos.quantidade_produto} unidades, estoque precisa estar zerado para excluir!", extra_tags='danger')

            return redirect('listar-produtos')
        
        else:
            request.method == 'POST'
            produtos.delete()
            messages.success(request, "Produto excluído com sucesso!")
            return redirect('listar-produtos')

    else:
        return redirect('login')
    
    
#funcao que calcula a entrada no estoque
def entradaEstoque(request, id):
    if request.session.get('usuario_logado'):
        
        produtos = get_object_or_404(Produto, id=id)
        if request.method == 'POST':
            quantidade_entrada = int(request.POST.get('quantidade_produto'))
            produtos.quantidade_produto += quantidade_entrada
            produtos.save()
            messages.success(request, "Entrada no estoque realizada com sucesso!")
            return redirect('listar-produtos')
        
    else:
        return redirect('login')