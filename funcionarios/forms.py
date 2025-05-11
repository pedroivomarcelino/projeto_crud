from django import forms
from funcionarios.models import Funcionario
from funcionarios.validators import (
    valida_cpf_existe,
    valida_tamanho_cpf,
    valida_tamanho_rg,
    valida_formato_telefone,
    valida_tamanho_cep
)

class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = [
            'nome_funcionario',
            'cpf_funcionario',
            'rg_funcionario',
            'endereco_funcionario',
            'cep_funcionario',
            'bairro_funcionario',
            'cidade_funcionario',
            'estado_funcionario',
            'telefone_funcionario',
            'salario_funcionario',
            'comissao_funcionario',
            'cargo_funcionario',
            'status_funcionario'
        ]
        
    def clean_cpf_funcionario(self):
        """Valida CPF (tamanho e existência no banco)."""
        cpf_funcionario = self.cleaned_data.get('cpf_funcionario')

        if self.instance and self.instance.cpf_funcionario == cpf_funcionario:
            return cpf_funcionario

        valida_tamanho_cpf(cpf_funcionario)  # Verifica se tem 14 dígitos
        valida_cpf_existe(cpf_funcionario)  # Verifica se já existe no banco
        return cpf_funcionario
    
    def clean_rg_funcionario(self):
        """Valida RG (tamanho)."""
        rg_funcionario = self.cleaned_data.get('rg_funcionario')
        valida_tamanho_rg(rg_funcionario)
        return rg_funcionario
    
    def clean_telefone_funcionario(self):
        """Valida o formato do telefone fixo."""
        telefone_funcionario = self.cleaned_data.get('telefone_funcionario')
        valida_formato_telefone(telefone_funcionario)
        return telefone_funcionario
    
    def clean_cep_funcionario(self):
        """Valida o formato do CEP."""
        cep_funcionario = self.cleaned_data.get('cep_funcionario')
        valida_tamanho_cep(cep_funcionario)
        return cep_funcionario