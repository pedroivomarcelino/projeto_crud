from django.db import models

class Produto(models.Model):
    codigo_produto = models.CharField(max_length=10, null=False, blank=False, unique=True)
    nome_produto = models.CharField(max_length=250, null=False, blank=False)
    modelo_produto = models.CharField(max_length=250, null=True, blank=True)
    fabricante_produto = models.CharField(max_length=250, null=True, blank=True)
    preco_produto = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    quantidade_produto = models.IntegerField(null=False, blank=False)
    descricao_produto = models.TextField(null=True, blank=True)
    
    
    def __str__(self):
        return self.nome_produto
    
