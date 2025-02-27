import re
from django.core.exceptions import ValidationError
from crud.models import Cliente

#validações clientes
def valida_cpf_existe(cpf_cnpj_cliente):
    """ Verifica se o CPF existe cadastrado no banco de dados"""
    if Cliente.objects.filter(cpf_cnpj_cliente=cpf_cnpj_cliente).exists():
        raise ValidationError("CPF já cadastrado no sistema")
    
def valida_tamanho_cpf(cpf_cnpj_cliente):
    """Verifica o tamanho do CPF se é igual ou maior que 14 digitos"""
    if len(cpf_cnpj_cliente) != 14:
        raise ValidationError("CPF deve conter 14 dígitos")
    
def valida_tamanho_rg(rg_cliente):
    """Verifica se o RG tem no máximo 12 dígitos, mas apenas se for preenchido"""
    if rg_cliente and rg_cliente.strip():  # Garante que não seja None ou string vazia
        if len(rg_cliente) > 12:
            raise ValidationError("RG deve conter até 12 dígitos")

def valida_formato_telefone(telefone_cliente):
    """Verifica o formato do telefone 99 9999-9999"""
    if not re.match(r'^\d{2} \d{4}-\d{4}$', telefone_cliente):
        raise ValidationError("Formato de telefone inválido. Digite no formato 99 9999-9999")

def valida_formato_clular(celular_cliente):
    """Verifica o formato do celular 99 99999-9999"""
    if not re.match(r'^\d{2} \d{5}-\d{4}$', celular_cliente):
        raise ValidationError("Formato de celular inválido. Digite no formato 99 99999-9999")
    
    
def valida_tamanho_cep(cep_cliente):
    """Verifica o tamanho do CEP se é igual ou maior que 9 digitos"""
    if len(cep_cliente) > 9:
        raise ValidationError("CEP deve conter até 9 dígitos")