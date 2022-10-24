from django.db import models
from django.utils import timezone


# Create your models here.

class Registry(models.Model):
    CHOICES = (
        ('Despesa', 'Despesa'),
        ('Receita', 'Receita')
    )

    CATEGORY = (
        ('Comida e Bebida', 'Comida e Bebida'),
        ('Compras', 'Compras'),
        ('Habilitacao', 'Habilitacao'),
        ('Transporte', 'Transporte'),
        ('Veiculo', 'Veiculo'),
        ('Vida e Entretenimento', 'Vida e Entretenimento'),
        ('Comunicacao, PC', 'Comunicacao, PC'),
        ('Despesas Financeiras', 'Despesas Financeiras'),
        ('Investimentos', 'Investimentos'),
        ('Renda', 'Renda'),
        ('Outro', 'Outro')
    )
    descricao = models.CharField(max_length=275, null=True)
    escolha = models.CharField(max_length=50, null=True, choices=CHOICES, default="Despesa")
    data_entrada = models.DateTimeField(default=timezone.now, null=True)
    quantia = models.FloatField()
    categoria = models.CharField(max_length=50, null=True, choices=CATEGORY)


class Investments(models.Model):
    TYPES = (
        ('Ações, BDR, ETFs, FIIs e Units', 'Ações, BDR, ETFs, FIIs e Units'),
        ('Fundos de Investimento', 'Fundos de Investimento'),
        ('Investimentos no Exterior', 'Investimentos no Exterior'),
        ('CDB / LCI / LCA / LC / LF', 'CDB / LCI / LCA / LC / LF'),
        ('CRI / CRA', 'CRI / CRA'),
        ('Debêntures', 'Debêntures'),
        ('Opções de Ações', 'Opções de Ações'),
        ('Termos de Ações', 'Termos de Ações'),
        ('Futuros', 'Futuros'),
        ('COE', 'COE'),
        ('Poupança', 'Poupança'),
        ('Moedas', 'Moedas'),
        ('Criptomoedas', 'Criptomoedas'),
        ('Ativos Genéricos', 'Ativos Genéricos'),
        ('Caixa', 'Caixa'),
        ('Commodities', 'Commodities'),
    )

    tipo = models.CharField(max_length=50, null=True, choices=TYPES)
    nome = models.CharField(max_length=40, null=True)
    taxa = models.FloatField(null=True)
    taxa_corretagem = models.FloatField(null=True)
    data_compra = models.DateTimeField(default=timezone.now, null=True)
    data_vencimento = models.DateTimeField(default=timezone.now, null=True)
    banco = models.CharField(max_length=40, null=True)
    corretora = models.CharField(max_length=40, null=True)
    quantidade = models.FloatField(null=True)


class Login(models.Model):
    nome = models.CharField(max_length=100, null=True)
    sobrenome = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=200, null=True)
    senha = models.CharField(max_length=30, null=True)
    repetir_senha = models.CharField(max_length=30, null=True)
