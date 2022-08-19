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


class Money(models.Model):
    description = models.CharField(max_length=255)
    select = models.CharField(max_length=30)
    choice = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    date = models.DateField
    amount = models.FloatField
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.select
