from django.shortcuts import render, redirect
from estoque.forms import ProdutoForm
from django.contrib import messages
from estoque.models import Produto


#carregar o form de cadastrar novos produtos no estoque
def cadastrarProdutos(request):
    return render(request, 'estoque/cadastrar_produto.html')



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