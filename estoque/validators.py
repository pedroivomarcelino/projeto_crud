import re
from django.core.exceptions import ValidationError
from estoque.models import Produto

#valida se o codigo do prouto já existe no banco de dados
def valida_codigo_produto_existe(codigo_produto):
    """Verifica se o código do produto já existe no banco de dados"""
    if Produto.objects.filter(codigo_produto=codigo_produto).exists():
        raise ValidationError("Código de produto já cadastrado no sistema")
    
#valida se o preco inserido do produto é maior que 0
"""Verifica se o preço do produto é maior que zero"""
def valida_valor_produto(preco_produto):
    if preco_produto < 0:
        raise ValidationError("Valor do produto não pode ser menor que zero")
    
    
#valida se a quantidade inserida do produto é maior que 0 no estoque
def valida_quantidade_produto_estoque(quantidade_produto):
    """Verifica se a quantidade do produto é maior que zero"""
    if quantidade_produto < 0:
        raise ValidationError("Quantidade do produto não pode ser menor que zero")