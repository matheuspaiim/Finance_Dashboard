from django.db import models
from django import forms
# Create your models here.

CHOICES = (
    ('expense', 'Despesa'),
    ('revenue', 'Receita')
)


class Category(models.Model):
    select = models.CharField(max_length=30)

    def __str__(self):
        return self.select


class Registro(models.Model):
    descricao = models.CharField(max_length=255)
    selecao = models.CharField(max_length=30)
    escolha = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    data_entrada = models.DateField
    quantia = models.FloatField
    categoria = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.selecao
