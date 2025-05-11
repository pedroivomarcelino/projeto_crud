import re
from django.core.exceptions import ValidationError
from funcionarios.models import Funcionario

def valida_cpf_existe(cpf_funcionario):
    """ Verifica se o CPF existe cadastrado no banco de dados"""
    if Funcionario.objects.filter(cpf_funcionario=cpf_funcionario).exists():
        raise ValidationError("CPF já cadastrado no sistema")
    
def valida_tamanho_cpf(cpf_funcionario):
    """Verifica o tamanho do CPF se é igual ou maior que 14 digitos"""
    if len(cpf_funcionario) > 14:
        raise ValidationError("CPF deve conter até 14 dígitos")
    
def valida_tamanho_rg(rg_funcionario):
    """Verifica se o RG tem no máximo 12 dígitos, mas apenas se for preenchido"""
    if rg_funcionario and rg_funcionario.strip():  # Garante que não seja None ou string vazia
        if len(rg_funcionario) > 12:
            raise ValidationError("RG deve conter até 12 dígitos")
        
def valida_formato_telefone(telefone_funcionario):
    """Verifica o formato do telefone 99 99999-9999"""
    if not re.match(r'^\d{2} \d{5}-\d{4}$', telefone_funcionario):
        raise ValidationError("Formato de telefone inválido. Digite no formato 99 9999-9999")
    
def valida_tamanho_cep(cep_funcionario):
    """Verifica o tamanho do CEP se é igual ou maior que 9 digitos"""
    if len(cep_funcionario) > 9:
        raise ValidationError("CEP deve conter até 9 dígitos")