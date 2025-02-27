from django.db import models

class Cliente(models.Model):
    nome_cliente = models.CharField(max_length=255, null=False, blank=False)
    cpf_cnpj_cliente = models.CharField(max_length=14, null=False, blank=False)
    rg_cliente = models.CharField(max_length=12, null=True, blank=True)
    endereco_cliente = models.CharField(max_length=255, null=False, blank=False)
    cep_cliente = models.CharField(max_length=9, null=False, blank=False)
    numero_cliente= models.CharField(max_length=10, null=False, blank=False)
    complemento_cliente = models.CharField(max_length=255, null=True, blank=True)
    bairro_cliente = models.CharField(max_length=100, null=False, blank=False)
    municipio_cliente = models.CharField(max_length=100, null=False, blank=False)
    cidade_cliente = models.CharField(max_length=100, null=False, blank=False)
    estado_cliente = models.CharField(max_length=30, null=False, blank=False)
    telefone_cliente = models.CharField(max_length=15, null=True, blank=True)
    celular_cliente = models.CharField(max_length=15, null=False, blank=False)
    email_cliente = models.EmailField(max_length=255, null=True, blank=True)
    
    def __str__(self):
        return self.nome_cliente