from django.db import models
from django import forms
from django.utils import timezone

# Create your models here.

class Registry(models.Model):
    CHOICES = (
        ('expense', 'Despesa'),
        ('revenue', 'Receita')
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
    descricao = models.CharField(max_length=255, null=True)
    escolha = models.CharField(max_length=50, null=True, choices=CHOICES)
    data_entrada = models.DateTimeField(default=timezone.now, null=True)
    quantia = models.FloatField()
    categoria = models.CharField(max_length=200, null=True, choices=CATEGORY)

