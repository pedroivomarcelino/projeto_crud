from django.db import models

class Funcionario(models.Model):
    CARGOS = [
        ('vendedor', 'Vendedor'),
        ('administrativo', 'Administrativo'),
    ]

    STATUS = [
        ('ativo', 'Ativo'),
        ('desativado', 'Desativado'),
    ]

    nome_funcionario = models.CharField(max_length=250, null=False, blank=False)
    cpf_funcionario = models.CharField(max_length=14, null=False, blank=False, unique=True)
    rg_funcionario = models.CharField(max_length=12, null=True, blank=True)
    endereco_funcionario = models.CharField(max_length=255, null=False, blank=False)
    bairro_funcionario = models.CharField(max_length=100, null=False, blank=False)
    cidade_funcionario = models.CharField(max_length=100, null=False, blank=False)
    telefone_funcionario = models.CharField(max_length=15, null=True, blank=True)
    salario_funcionario = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    comissao_funcionario = models.IntegerField(null=True, blank=True)
    cargo_funcionario = models.CharField(max_length=100, choices=CARGOS, null=False, blank=False)
    status_funcionario = models.CharField(max_length=100, choices=STATUS, default='ativo', null=False, blank=False)

    def __str__(self):
        return self.nome_funcionario
