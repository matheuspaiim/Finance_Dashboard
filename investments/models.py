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


class Login(models.Model):
    nome = models.CharField(max_length=100, null=True)
    sobrenome = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=200, null=True)
    senha = models.CharField(max_length=30, null=True)
    repetir_senha = models.CharField(max_length=30, null=True)
