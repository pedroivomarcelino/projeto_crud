from django.shortcuts import render

def cadastrarProdutos(request):
    return render(request, 'estoque/cadastrar_produto.html')
