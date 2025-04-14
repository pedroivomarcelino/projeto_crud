from django.shortcuts import render, redirect, get_object_or_404
from estoque.forms import ProdutoForm
from django.contrib import messages
from estoque.models import Produto


#carregar o form de cadastrar novos produtos no estoque
def cadastrarProdutos(request):
    return render(request, 'estoque/cadastrar_produto.html')


#carregar o form de vizualizacao dos produtos cadastrados no estoque
def vizualizarProdutos(request, id):
   produtos = Produto.objects.get(id=id)
   return render(request, 'estoque/visualisar_produto.html', {'produtos': produtos})


#carrega o form de edicao de produtos
def editarProdutos(request, id):
    produtos = Produto.objects.get(id=id)
    return render(request, 'estoque/editar_produto.html', {'produtos': produtos})


#funcao para inserir novos produtos no banco de dados
def inserirProduto(request):

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


#funcao para atualizar os produtos cadastrados no banco de dados
def updateProdutos(request, id):
    
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
                    