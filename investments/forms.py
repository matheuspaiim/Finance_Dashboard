from django.forms import ModelForm
from .models import Registry, Login
from django import forms


class RegistryForm(ModelForm):
    class Meta:
        model = Registry
        fields = ['descricao', 'escolha', 'data_entrada', 'quantia', 'categoria']

        exclude = ()

        widgets = {
            'descricao': forms.TextInput(attrs={'class': 'input--style-4', 'autofocus': ''}),
            'escolha': forms.RadioSelect(attrs={'class': 'input--style-4'}),
            'data_entrada': forms.DateInput(attrs={'class': 'input--style-4'}),
            'quantia': forms.NumberInput(attrs={'class': 'input--style-4'}),
            'categoria': forms.Select(attrs={'class': 'input--style-4'}),
        }


class LoginForm(ModelForm):
    class Meta:
        model = Login
        exclude = ()

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control form-control-user', 'autofocus': ''}),
            'sobrenome': forms.TextInput(attrs={'class': 'form-control form-control-user'}),
            'email': forms.TextInput(attrs={'class': 'form-control form-control-user'}),
            'senha': forms.TextInput(attrs={'class': 'form-control form-control-user'}),
        }