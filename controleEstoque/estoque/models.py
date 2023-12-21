from django.db import models


class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Produto(models.Model):
    nome = models.CharField(max_length=100, unique=True, verbose_name="Nome do produto")
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=0)
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Preço Unitário", blank=True)
    data_alteracao = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.nome
