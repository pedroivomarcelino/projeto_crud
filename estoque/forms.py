from django import forms
from estoque.models import Produto
from estoque.validators import valida_codigo_produto_existe, valida_valor_produto, valida_quantidade_produto_estoque

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = [
            'codigo_produto',
            'nome_produto',
            'modelo_produto',
            'fabricante_produto',
            'preco_produto',
            'quantidade_produto',
            'descricao_produto'
        ]
        
        
    def clean_codigo_produto(self):
        """Verifica se o código do produto já existe no banco de dados"""
        codigo_produto = self.cleaned_data.get('codigo_produto')
        
        if self.instance and self.instance.codigo_produto == codigo_produto:
            return codigo_produto
        
        valida_codigo_produto_existe(codigo_produto)
        return codigo_produto
    
    
    def clean_preco_produto(self):
        """Verificar se o preço do produto é maior que zero"""
        preco_produto = self.cleaned_data.get('preco_produto')
        
        valida_valor_produto(preco_produto)
        return preco_produto
    
    def clean_quantidade_produto(self):
        """Verifica se a quantidade do produto é maior que zero"""
        quantidade_produto = self.cleaned_data.get('quantidade_produto')

        valida_quantidade_produto_estoque(quantidade_produto)
        return quantidade_produto