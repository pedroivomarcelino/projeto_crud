from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages



def cadastrarFuncionarios(request):
    if request.session.get('usuario_logado'):
        return render(request, 'funcionarios/cadastrar_funcionarios.html')
        
    else:
        return redirect('login')
