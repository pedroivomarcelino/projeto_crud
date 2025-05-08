from django import forms
from funcionarios.models import Funcionario

class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = [
            'nome_funcionario',
            'cpf_funcionario',
            'rg_funcionario',
            'endereco_funcionario',
            'bairro_funcionario',
            'cidade_funcionario',
            'telefone_funcionario',
            'salario_funcionario',
            'comissao_funcionario',
            'cargo_funcionario',
            'status_funcionario'
        ]