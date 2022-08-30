from django.db import models
from django import forms
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
    descricao = models.CharField(max_length=255)
    selecao = models.CharField(max_length=30)
    escolha = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    data_entrada = models.DateTimeField(auto_now_add=True, null=True)
    quantia = models.FloatField
    categoria = models.ForeignKey(CATEGORY, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.selecao
