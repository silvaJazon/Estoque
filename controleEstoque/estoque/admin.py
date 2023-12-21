from django.contrib import admin
from openpyxl import Workbook
from django.http import HttpResponse
from .models import Categoria, Produto


def exportar_para_excel(modeladmin, request, queryset):
    # Criar um workbook e adicionar uma planilha
    wb = Workbook()
    ws = wb.active

    # Adicionar cabeçalhos
    ws.append(['Nome', 'Categoria', 'Quantidade', 'Preço Unitário',])

    # Adicionar dados
    for produto in queryset:
        ws.append(
            [produto.nome, produto.categoria.nome, produto.quantidade, produto.preco_unitario,])

    # Criar uma resposta HTTP com o conteúdo do arquivo Excel
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=produtos.xlsx'

    # Salvar o workbook na resposta
    wb.save(response)

    return response


exportar_para_excel.short_description = "Exportar para Excel"


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'categoria', 'quantidade', 'preco_unitario', 'data_alteracao')
    list_filter = ('categoria',)
    search_fields = ('nome', 'categoria__nome',)
    ordering = ('-data_alteracao',)
    actions = [exportar_para_excel]


admin.site.register(Categoria)
admin.site.register(Produto, ProdutoAdmin)
