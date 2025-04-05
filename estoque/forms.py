from django import forms
from estoque.models import Produto

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
    