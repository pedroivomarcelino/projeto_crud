from django import forms
from crud.models import Cliente
from crud.validators import (
    valida_cpf_existe, 
    valida_formato_clular, 
    valida_formato_telefone, 
    valida_tamanho_cep, 
    valida_tamanho_cpf, 
    valida_tamanho_rg
)

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = [
            'nome_cliente',
            'cpf_cnpj_cliente',
            'rg_cliente',
            'endereco_cliente',
            'cep_cliente',
            'numero_cliente',
            'complemento_cliente',
            'bairro_cliente',
            'municipio_cliente',
            'cidade_cliente',
            'estado_cliente',
            'telefone_cliente',
            'celular_cliente',
            'email_cliente'
        ]

    def clean_cpf_cnpj_cliente(self):
        """Valida CPF (tamanho e existência no banco)."""
        cpf_cnpj_cliente = self.cleaned_data.get('cpf_cnpj_cliente')
        
        if self.instance and self.instance.cpf_cnpj_cliente == cpf_cnpj_cliente:
            return cpf_cnpj_cliente 
        
        valida_tamanho_cpf(cpf_cnpj_cliente)  # Verifica se tem 14 dígitos
        valida_cpf_existe(cpf_cnpj_cliente)  # Verifica se já existe no banco
        return cpf_cnpj_cliente

    def clean_rg_cliente(self):
        """Valida RG (tamanho)."""
        rg_cliente = self.cleaned_data.get('rg_cliente')
        valida_tamanho_rg(rg_cliente)
        return rg_cliente

    def clean_telefone_cliente(self):
        """Valida o formato do telefone fixo."""
        telefone_cliente = self.cleaned_data.get('telefone_cliente')
        if telefone_cliente:  # Evita erro caso o campo não seja obrigatório
            valida_formato_telefone(telefone_cliente)
        return telefone_cliente

    def clean_celular_cliente(self):
        """Valida o formato do celular."""
        celular_cliente = self.cleaned_data.get('celular_cliente')
        valida_formato_clular(celular_cliente)
        return celular_cliente

    def clean_cep_cliente(self):
        """Valida o tamanho do CEP."""
        cep_cliente = self.cleaned_data.get('cep_cliente')
        valida_tamanho_cep(cep_cliente)
        return cep_cliente
