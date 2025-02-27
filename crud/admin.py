from django.contrib import admin
from crud.models import Cliente

class ListandoClientes(admin.ModelAdmin):
    list_display = (
        "id",
        "nome_cliente",
        "cpf_cnpj_cliente",
        "rg_cliente",
        "endereco_cliente",
        "cep_cliente",
        "numero_cliente",
        "complemento_cliente",
        "bairro_cliente",
        "municipio_cliente",
        "cidade_cliente",
        "estado_cliente",
        "telefone_cliente",
        "celular_cliente",
        "email_cliente"
    )
    list_display_links = ("id", "nome_cliente")
    search_fields = ("nome_cliente", "cpf_cnpj_cliente")
    list_per_page = 30
    
admin.site.register(Cliente, ListandoClientes)
